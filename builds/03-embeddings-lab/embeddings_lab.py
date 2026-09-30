"""Five small experiments: geometry, pairs, retrieval, chunking, and evaluation."""

import argparse
import json
import math
from pathlib import Path
import re
import sys
import time


DATA_DIR = Path(__file__).resolve().parent / "data"
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_QUERY = "I forgot my password. How can I get back into my account?"
CHUNK_QUERY = "What is the maximum attachment size in a support ticket?"


def validate_vectors(left, right):
    if len(left) == 0 or len(left) != len(right):
        raise ValueError("Vectors must have equal, nonzero dimensions")
    if not all(math.isfinite(value) for value in [*left, *right]):
        raise ValueError("Vectors must contain finite numbers")


def dot(left, right):
    validate_vectors(left, right)
    return sum(a * b for a, b in zip(left, right))


def cosine(left, right):
    numerator = dot(left, right)
    denominator = math.sqrt(dot(left, left) * dot(right, right))
    if denominator == 0:
        raise ValueError("Cosine is undefined for a zero vector")
    return numerator / denominator


def euclidean(left, right):
    validate_vectors(left, right)
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def rank_scores(ids, scores, k):
    if k < 1 or len(ids) != len(scores) or len(set(ids)) != len(ids):
        raise ValueError("Ranking needs unique IDs, one score per ID, and k >= 1")
    if not all(math.isfinite(score) for score in scores):
        raise ValueError("Ranking scores must be finite")
    return sorted(zip(ids, map(float, scores)), key=lambda row: (-row[1], row[0]))[:k]


def keyword_score(query, text):
    """Fraction of distinct query tokens present; deliberately simpler than BM25."""
    terms = set(re.findall(r"\w+", query.casefold()))
    words = set(re.findall(r"\w+", text.casefold()))
    return len(terms & words) / len(terms) if terms else 0.0


def retrieval_metrics(ranked_ids, relevant_ids, k):
    relevant = set(relevant_ids)
    if not relevant or k < 1 or len(set(ranked_ids)) != len(ranked_ids):
        raise ValueError("Metrics need relevant IDs, unique ranked IDs, and k >= 1")
    first = next((i for i, item in enumerate(ranked_ids, 1) if item in relevant), None)
    return {
        "recall_at_k": len(set(ranked_ids[:k]) & relevant) / len(relevant),
        "reciprocal_rank_at_k": 1 / first if first is not None and first <= k else 0.0,
        "first_relevant_rank": first,
    }


def document_text(document):
    return document["title"] + "\n" + document["text"]


def paragraph_chunks(documents):
    chunks = []
    for document in documents:
        for number, paragraph in enumerate(document["text"].split("\n\n"), 1):
            if paragraph.strip():
                chunks.append({
                    "id": f"{document['id']}-p{number:02}",
                    "source_id": document["id"],
                    "title": document["title"],
                    "text": paragraph.strip(),
                })
    return chunks


def validate_dataset(documents, queries):
    ids = [document["id"] for document in documents]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("Document IDs must be nonempty and unique")
    for document in documents:
        if not all(document[field].strip() for field in ("id", "title", "text")):
            raise ValueError("Every document needs an ID, title, and text")
    query_ids, query_texts = set(), set()
    for split in ("dev", "test", "no_answer"):
        if not queries.get(split):
            raise ValueError(f"Missing queries for {split}")
        for query in queries[split]:
            normalized = " ".join(query["text"].casefold().split())
            if not normalized or query["id"] in query_ids or normalized in query_texts:
                raise ValueError("Query IDs and normalized texts must be unique across splits")
            query_ids.add(query["id"])
            query_texts.add(normalized)
            relevant = query.get("relevant_ids", [])
            if split == "no_answer":
                if relevant:
                    raise ValueError("No-answer probes must not have relevant IDs")
            elif not relevant or not set(relevant) <= set(ids) or len(set(relevant)) != len(relevant):
                raise ValueError("Each answerable query needs unique, existing relevant IDs")


def load_data():
    documents = json.loads((DATA_DIR / "support_docs.json").read_text())
    queries = json.loads((DATA_DIR / "queries.json").read_text())
    validate_dataset(documents, queries)
    return documents, queries


def geometry_example():
    print("\nGEOMETRY: MANUAL VECTORS (not learned text embeddings)")
    query = [1.0, 0.0]
    print(f"Query = {query}; larger cosine/dot and smaller distance mean closer.")
    print(f"{'candidate':12} {'cosine':>9} {'dot':>9} {'distance':>9}")
    for name, vector in [("nearby", [0.8, 0.6]), ("scaled", [8, 6]), ("opposite", [-1, 0])]:
        print(f"{name:12} {cosine(query, vector):9.4f} {dot(query, vector):9.4f} {euclidean(query, vector):9.4f}")
    scaled = [8, 6]
    normalized = [value / math.sqrt(dot(scaled, scaled)) for value in scaled]
    print(f"Normalized scaled vector = {normalized}; dot = cosine = {dot(query, normalized):.4f}")
    print("Try changing vector magnitude and direction separately. Zero-vector cosine is undefined.")


def load_model(name, revision):
    # Geometry, fixture checks, and offline tests never import third-party packages.
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as error:
        raise RuntimeError("Install this lab's requirements.txt before running learned examples") from error
    options = {"device": "cpu"}
    if revision:
        options["revision"] = revision
    start = time.perf_counter()
    model = SentenceTransformer(name, **options)
    print(f"Model: {name}; requested revision: {revision or 'default branch (unpinned)'}; device: cpu")
    print(f"Dimensions: {model.get_embedding_dimension()}; max sequence length: {model.max_seq_length}")
    print(f"Model load: {time.perf_counter() - start:.2f}s (first run may download weights)")
    return model


def encode_documents(model, documents):
    return model.encode_document(
        [document_text(document) for document in documents],
        normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False,
    )


def learned_ranking(model, query, documents, vectors, k, timings=None):
    start = time.perf_counter()
    query_vector = model.encode_query(
        [query], normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False,
    )[0]
    encoded_at = time.perf_counter()
    # Unit-length vectors make dot product equal cosine; exact scan is enough for 24 records.
    scores = [dot(query_vector, vector) for vector in vectors]
    ranking = rank_scores([document["id"] for document in documents], scores, k)
    if timings is not None:
        timings["query_encoding"] += encoded_at - start
        timings["scoring"] += time.perf_counter() - encoded_at
    return ranking


def keyword_ranking(query, documents, k):
    return rank_scores(
        [document["id"] for document in documents],
        [keyword_score(query, document_text(document)) for document in documents], k,
    )


def print_ranking(label, ranking, documents):
    by_id = {document["id"]: document for document in documents}
    print(label)
    for number, (doc_id, score) in enumerate(ranking, 1):
        document = by_id[doc_id]
        source = f" source={document['source_id']}" if "source_id" in document else ""
        print(f"  {number}. {doc_id}{source} score={score:.4f} | {document['title']}")
        print(f"     {document['text'][:150].replace(chr(10), ' ')}")


def pairs_example(model):
    print("\nPAIRS: inspect relatedness, including a negation trap")
    texts = [
        "I forgot my password and cannot sign in.",
        "How do I reset a password I cannot remember?",
        "Where can I download last month's invoice?",
        "I did not forget my password and I can sign in.",
    ]
    vectors = model.encode(texts, normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)
    norms = [math.sqrt(dot(vector, vector)) for vector in vectors]
    print(f"Embedding matrix shape: {vectors.shape}; anchor: {texts[0]}")
    print(f"Measured norm range: min={min(norms):.6f}, max={max(norms):.6f}; anchor norm={norms[0]:.6f}")
    for label, text, vector, norm in zip(["paraphrase", "unrelated", "negation"], texts[1:], vectors[1:], norms[1:]):
        print(f"  {label:10} cosine={dot(vectors[0], vector):.4f} norm={norm:.6f} | {text}")
    print("A high score measures this model's similarity; it does not establish logical equivalence.")


def search_example(model, documents, query, k):
    print(f"\nSEARCH: {query}")
    start = time.perf_counter()
    vectors = encode_documents(model, documents)
    print(f"Document encoding: {time.perf_counter() - start:.4f}s; documents={len(documents)}; shape={vectors.shape}")
    start = time.perf_counter()
    keyword = keyword_ranking(query, documents, k)
    print(f"Keyword scoring and ranking: {time.perf_counter() - start:.4f}s")
    timings = {"query_encoding": 0.0, "scoring": 0.0}
    learned = learned_ranking(model, query, documents, vectors, k, timings)
    print(f"Query encoding: {timings['query_encoding']:.4f}s")
    print(f"Learned scoring and ranking: {timings['scoring']:.4f}s (model loading excluded)")
    print_ranking("Keyword baseline (query-token overlap)", keyword, documents)
    print_ranking("Learned retrieval (cosine)", learned, documents)
    print("These are different score scales, neither calibrated as answer confidence.")


def chunking_example(model, documents, query, k):
    print(f"\nCHUNKING: {query}")
    handbook = {"id": "handbook", "title": "Support handbook",
                "text": "\n\n".join(document_text(document) for document in documents)}
    chunks = paragraph_chunks([handbook])
    # Keep the answer-bearing final paragraph late in the long input on purpose.
    full_text = document_text(handbook)
    token_ids = model.tokenizer(full_text, truncation=False, add_special_tokens=True, verbose=False)["input_ids"]
    retained_ids = model.tokenizer(full_text, truncation=True, max_length=model.max_seq_length, verbose=False)["input_ids"]
    retained_text = model.tokenizer.decode(retained_ids).casefold()
    print(f"Whole handbook: {len(token_ids)} tokens; model limit: {model.max_seq_length}; retained: {len(retained_ids)}")
    print(f"Attachment answer marker '20 mb' survives prefix truncation: {'20 mb' in retained_text}")
    print("The untruncated count is a diagnostic only; document encoding applies the model's input limit.")
    counts = [len(model.tokenizer(document_text(chunk), truncation=False, verbose=False)["input_ids"]) for chunk in chunks]
    print(f"Paragraph chunks: {len(chunks)}; token counts: min={min(counts)}, max={max(counts)}")
    print(f"Chunks over limit: {sum(count > model.max_seq_length for count in counts)}; title is repeated in each input")
    print("Token counts here omit any model-added retrieval prompt; the default model has no such prompt.")
    whole_docs = [handbook]
    print_ranking("Whole-document retrieval (one candidate)", learned_ranking(model, query, whole_docs, encode_documents(model, whole_docs), k), whole_docs)
    print_ranking("Paragraph retrieval", learned_ranking(model, query, chunks, encode_documents(model, chunks), k), chunks)
    print("Compare available answer text, not scores across these candidate sets. More chunks are not automatically better.")


def evaluate_example(model, documents, queries, split, k):
    selected = queries[split]
    print(f"\nEVALUATE: split={split}, answerable queries={len(selected)}, k={k}")
    print("Per-query recall = relevant retrieved / all labeled relevant; RR@k = 1/first rank within k, else 0.")
    print("Aggregate Recall@k and MRR@k are macro means over answerable queries; no-answer probes are excluded.")
    start = time.perf_counter()
    vectors = encode_documents(model, documents)
    print(f"Document encoding: {time.perf_counter() - start:.4f}s; documents={len(documents)}")
    print("Query/scoring timing totals cover answerable queries only; model loading and no-answer probes are excluded.")
    for method in ("keyword", "learned"):
        values = []
        timings = {"query_encoding": 0.0, "scoring": 0.0}
        print(f"\n{method}: query ID | first relevant rank | Recall@{k} | RR@{k} | top IDs")
        for query in selected:
            if method == "keyword":
                start = time.perf_counter()
                ranking = keyword_ranking(query["text"], documents, len(documents))
                timings["scoring"] += time.perf_counter() - start
            else:
                ranking = learned_ranking(model, query["text"], documents, vectors, len(documents), timings)
            ranked_ids = [doc_id for doc_id, _ in ranking]
            metrics = retrieval_metrics(ranked_ids, query["relevant_ids"], k)
            values.append(metrics)
            print(f"  {query['id']} | {metrics['first_relevant_rank']} | {metrics['recall_at_k']:.3f} | {metrics['reciprocal_rank_at_k']:.3f} | {', '.join(ranked_ids[:k])}")
        recall = sum(value["recall_at_k"] for value in values) / len(values)
        mrr = sum(value["reciprocal_rank_at_k"] for value in values) / len(values)
        print(f"  {method} mean Recall@{k}={recall:.3f}; MRR@{k}={mrr:.3f}; denominator={len(values)} queries")
        if method == "learned":
            print(f"  Query encoding: {timings['query_encoding']:.4f}s total for {len(selected)} queries")
            print(f"  Learned scoring and ranking: {timings['scoring']:.4f}s total")
        else:
            print(f"  Keyword scoring and ranking: {timings['scoring']:.4f}s total")
    print("\nNo-answer probes: exact top-k still returns a candidate. No abstention threshold is configured.")
    for query in queries["no_answer"]:
        print(f"  {query['id']}: {query['text']}")
        for method, ranking in [
            ("keyword", keyword_ranking(query["text"], documents, 1)),
            ("learned", learned_ranking(model, query["text"], documents, vectors, 1)),
        ]:
            print(f"    {method}: {ranking[0][0]} score={ranking[0][1]:.4f}; label=no answer in corpus")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--example", choices=["geometry", "pairs", "search", "chunking", "evaluate", "all"], default="geometry")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--revision", help="Model repository revision (use a commit SHA to pin weights)")
    parser.add_argument("--query", help="Custom search/chunking query (ignored by fixed labeled evaluation)")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--split", choices=["dev", "test"], default="dev")
    parser.add_argument("--check", action="store_true", help="Validate bundled fixtures without loading a model")
    args = parser.parse_args(argv)
    if args.top_k < 1:
        parser.error("--top-k must be at least 1")
    if args.query is not None and not args.query.strip():
        parser.error("--query must not be blank")
    if args.check:
        documents, queries = load_data()
        print(f"Fixture check passed: {len(documents)} documents; "
              f"{len(queries['dev'])} dev; {len(queries['test'])} test; {len(queries['no_answer'])} no-answer probes")
        return 0
    if args.example in ("geometry", "all"):
        geometry_example()
    if args.example == "geometry":
        return 0
    documents, queries = load_data()
    try:
        model = load_model(args.model, args.revision)
    except (ImportError, RuntimeError, OSError, ValueError) as error:
        print(f"Model loading failed: {error}\nNo substitute embeddings were used.", file=sys.stderr)
        return 1
    if args.example in ("pairs", "all"):
        pairs_example(model)
    if args.example in ("search", "all"):
        search_example(model, documents, args.query or DEFAULT_QUERY, args.top_k)
    if args.example in ("chunking", "all"):
        chunking_example(model, documents, args.query or CHUNK_QUERY, args.top_k)
    if args.example in ("evaluate", "all"):
        evaluate_example(model, documents, queries, args.split, args.top_k)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
