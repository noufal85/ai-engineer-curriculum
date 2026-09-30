# Embeddings lab

Run five small experiments, explain what each output shows, then change one variable and measure the result. This is a **local lab**: one Python program, synthetic support articles, and a local pretrained embedding model. It needs no API key or Docker service. The geometry example and dataset checks use only the standard library. The other examples use actual model inference on CPU.

Read the [embeddings chapter](../../docs/curriculum/03-embeddings.md) and [guided lab](../../docs/labs/03-embeddings.md) alongside the program.

## Run first: no download required

From the repository root, use its existing Python environment:

```bash
./.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py
./.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --check
```

The first command uses **manual vectors, not learned embeddings**. The `nearby` and `scaled` vectors both have cosine `0.8000`, but their dot products are `0.8000` and `8.0000`. Scaling changes magnitude without changing direction. The dataset check reports 24 documents, 8 development queries, 8 test queries, and 3 no-answer probes.

## Install the learned examples

Use a separate lab environment so model dependencies do not alter the documentation environment:

```bash
./.venv/bin/python -m venv builds/03-embeddings-lab/.venv
builds/03-embeddings-lab/.venv/bin/python -m pip install -r builds/03-embeddings-lab/requirements.txt
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example pairs
```

The first learned run needs internet access to download `sentence-transformers/all-MiniLM-L6-v2`. Later runs reuse the Hugging Face cache; set `HF_HUB_OFFLINE=1` when you want to require already-cached files. Package and model caches consume disk space. There is no API usage charge. Inference uses the synthetic local text; the program does not send it to a hosted inference service.

The requirements pin Sentence Transformers to `6.1.0`. Dependency versions underneath it can still vary. The default model's loaded weights produce 384-dimensional vectors and accept up to 256 tokens. The program prints the observed dimension, model limit, and requested revision so a model change is visible. `--revision` is optional; omitting it uses the model repository's current default branch. For an exact model revision used during this lab's validation:

```bash
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example all --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41
```

When choosing a different `--model`, choose a revision from that model's own repository. A reproducibility record should include the model ID and SHA, Python/package versions, input data version, query/document preparation, normalization, split, and `k`. Model rankings are observations, not expected constants in the offline tests.

## Five examples

The commands below run from the repository root. Read the prediction prompt before running each experiment.

| Example | Predict first | Inspect | Try changing |
|---|---|---|---|
| `geometry` | Does multiplying a vector by ten change its direction? | Cosine, dot product, Euclidean distance, normalized dot | Edit a manual vector's magnitude, then its direction |
| `pairs` | Will negating a sentence make it unrelated to the original? | Actual vector norms and paraphrase, unrelated, and negated sentence scores against one anchor | Replace the pair texts; inspect rather than assume the order |
| `search` | Which article answers a question without sharing its exact wording? | Keyword-overlap and learned cosine rankings, article IDs and excerpts | Query wording and `--top-k` |
| `chunking` | Can the whole handbook represent an answer near its end? | Actual token counts, truncation, full-document and paragraph results | Move the attachment paragraph earlier; inspect whether its answer survives |
| `evaluate` | Does a better first result also imply better recall? | Per-query ranks, Recall@k, MRR@k, and separate no-answer probes | Choose `k` on `dev`, then report the frozen choice on `test` |

```bash
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example pairs
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example search
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example search --query "HTTP 429" --top-k 5
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example chunking
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example evaluate --split dev --top-k 3
builds/03-embeddings-lab/.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example evaluate --split test --top-k 3
```

`--example all` runs all five; `--query` changes search and chunking inputs, while evaluation always uses the labeled queries. `--check` validates fixtures and exits without loading a model. `--help` lists every option. Default execution runs only geometry. A missing package or failed model load stops the learned examples; the program never substitutes hand-written or random embeddings.

Search and evaluation print document encoding, query encoding, and scoring/ranking times separately. Evaluation's query and scoring totals cover the selected answerable queries; model loading and no-answer probes are excluded. These measurements describe your particular run, including warm-up and cache effects, and are not benchmark guarantees.

## How the program works

- `data/support_docs.json` contains 24 fictional support articles with stable IDs, titles, and body text. They describe an invented product; they are not documentation for a real service.
- `data/queries.json` contains separate development and test queries with `relevant_ids`. Three no-answer probes carry no relevant IDs. All text and labels were authored for this lab; no customer data or downloaded corpus is used.
- Pair comparisons use `model.encode`. Retrieval uses `model.encode_document` for article title plus body and `model.encode_query` for the question. Inputs are batched and embeddings normalized. For the default model there are no separate query/document prompts; other models can have them.
- Retrieval performs an exact scan: dot product between normalized vectors equals cosine similarity. Scores sort descending, then by ID for stable ties. There is no vector database or approximate index.
- The keyword baseline measures the fraction of distinct, casefolded query tokens present in the article's title and body. It uses no stemming, stop-word removal, or term weighting. It is deliberately simpler than BM25. Its score scale is different from cosine.
- The chunking example concatenates the articles into a long handbook. The last paragraph includes the 20 MB attachment answer. It reports tokenizer counts and whether the answer marker survives prefix truncation, then compares the single whole-document candidate with paragraph candidates. Each chunk retains `source_id=handbook` and the handbook title. This isolates lost input and candidate granularity; a one-candidate whole-document rank cannot establish retrieval quality.

## What the evaluation means

For a query with relevant IDs `{a, b}` and ranking `[x, b, a]`, at `k=2`:

- Recall@2 is `1/2`: one of the two relevant articles appears in the first two results.
- Reciprocal rank@2 is `1/2`: the first relevant article appears at rank two.

If the first relevant result lies below `k`, reciprocal rank@k is zero. The printed first relevant rank may still show its position in the full ranking. **Mean Recall@k and MRR@k average the per-query values over the eight answerable queries in the selected split.** These are document-level metrics with complete labels for this small authored exercise, not an estimate of production accuracy. Changing `k` affects what is measured; report it with the results.

No-answer probes are printed separately for both baselines and excluded from these averages. Top-k always returns something when candidates exist. Neither a high cosine score nor a positive keyword score proves that the corpus can answer the question. The lab does not implement a calibrated abstention threshold.

Use `dev` for experiments. Freeze your model, text preparation, and `k` before looking at `test`. Repeatedly optimizing against the test results turns that split into another development set. Eight queries per split are enough to learn the workflow, not to select a production model reliably.

## Acceptance checks and deliberate failures

Run the offline regression checks with the repository's documentation environment:

```bash
./.venv/bin/python -m unittest discover -s tests -p test_embeddings_lab.py
```

These checks cover numerical geometry, stable ties, metric denominators and cutoffs, invalid input, fixture labels and split separation, source metadata, and CLI execution with third-party imports disabled. They do not assert learned rankings.

For the learned portion, complete all five examples and record the actual model revision, vector shape, query rankings, token counts, per-query failures, and aggregate metrics. The acceptance criterion is an explainable, measured result—not a preselected score. Keep the first run's observations as a baseline before editing.

Deliberately investigate at least three failures:

1. **Negation:** explain why a high similarity between opposite statements can still occur in the `pairs` experiment.
2. **Truncation:** show that the attachment answer is absent from the retained whole-handbook prefix and available in a paragraph chunk. Inspect the retrieved text; do not claim success from its score alone.
3. **Missing knowledge:** use `--example search --query "Do you offer a student discount?"`. Find the absent answer in the fixtures and explain why top-k still returns articles.

Also try `--top-k 0`: it must exit with an argument error before any model load. For an operational failure, run a learned example in a fresh environment without installing requirements; it must report the missing dependency and stop.

## Extend the experiment

Compare two configurations on the same frozen query set: for example, title-plus-body versus body only, or the default embedding model versus a second model. Re-embed both documents and queries for each model; never mix vectors from different model spaces. Record Recall@k, MRR@k, embedding time, dimensions, and three inspected failures. Do not compare raw similarity values between models as if they shared a confidence scale.

For a larger project, replace the synthetic labels with independently judged queries, compare against a stronger keyword baseline, test domain and multilingual examples, then decide whether caching, chunk overlap, reranking, or an index actually helps. Keep those infrastructure changes outside this small concept lab.
