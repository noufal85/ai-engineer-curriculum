# Lab 3 · Embeddings

**Chapter:** [Embeddings · From vectors to semantic search](../curriculum/03-embeddings.md) · **Code:** [`builds/03-embeddings-lab`](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/03-embeddings-lab) · **Format:** local Python lab

Build and inspect a search system over 24 synthetic support articles. Five examples move from hand-designed vectors to real local model inference and retrieval evaluation. No Docker service, API key, hosted embedding request, or vector database is required. The first model run downloads public model files, so allow additional time and disk space for setup.

## What you will be able to do

- Compare cosine, dot product, and Euclidean distance with actual numbers.
- Generate normalized sentence vectors and explain their shape.
- Compare lexical and embedding retrieval on the same corpus.
- Observe the effect of truncation and chunk boundaries.
- Evaluate answerable queries with Recall@k and MRR@k while keeping no-answer probes separate.
- Record a model/configuration choice with evidence and three known limitations.

## Setup

Run all commands from the repository root. The geometry example and local fixture checks need only the existing repository Python:

```bash
./.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --example geometry
./.venv/bin/python builds/03-embeddings-lab/embeddings_lab.py --check
```

For the four model examples, create a separate environment so their ML dependencies do not alter the documentation environment:

```bash
./.venv/bin/python -m venv builds/03-embeddings-lab/.venv
source builds/03-embeddings-lab/.venv/bin/activate
python -m pip install -r builds/03-embeddings-lab/requirements.txt
```

The commands below assume that environment remains active. The default model is `sentence-transformers/all-MiniLM-L6-v2`. The script accepts `--model` and `--revision` for an explicit model choice and revision. A model name alone does not freeze remote files; record the revision when you need a reproducible comparison. This revision was used to verify the model's dimensions and input limit while preparing the lab:

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example pairs \
  --model sentence-transformers/all-MiniLM-L6-v2 \
  --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41
```

Follow the selected model's input instructions and license before using an alternative.

The corpus lives in `builds/03-embeddings-lab/data/support_docs.json`; labeled development/test queries and separate no-answer probes live in `data/queries.json`. Read a few source articles before interpreting retrieval scores. Their policies are invented for this lab.

## Trial · A confident-looking wrong match (~15 min)

**1. Predict.** Run the geometry example and explain why raw dot product and cosine need not agree. The example uses invented coordinates; it is not a substitute for the model examples.

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example geometry
```

**2. Run an answerable search.** Predict a relevant support article, then inspect both rankings and the returned text:

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example search \
  --query "I forgot my password. How can I sign in again?" --top-k 3
```

**3. Deliberately ask for missing information.** First check the corpus and confirm that it does not contain an answer to this question:

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example search \
  --query "What is the weather on Mars tomorrow?" --top-k 3
```

The program still produces a ranking: top-*k* search selects candidates even when the corpus cannot answer. That is the deliberate failure. Read the top result and write why it is insufficient. Do not treat a positive similarity score as permission to invent an answer.

**4. Change one thing.** Use `--top-k 1` for the same missing-answer question. Did returning fewer candidates create evidence that was absent before? Record the top ID and score for both runs.

First-time downloads and installation are outside the 15-minute trial estimate. `--check` validates dataset structure, IDs, label references, and split overlap. It does not run model inference or establish retrieval quality.

## Example 1 · Geometry and normalization

**Predict:** Will a candidate with a larger magnitude always be a better directional match?

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example geometry
```

**Observe:** Compare dot products, cosine scores, and distances. Work through one calculation yourself using the formula in the [chapter](../curriculum/03-embeddings.md#5-measure-similarity-deliberately). Explain which measures prefer larger scores and which prefer smaller ones.

**Change:** Make a scratch copy of the geometry calculation and multiply one candidate's coordinates by a positive constant. Recalculate. The cosine should stay the same while the raw dot product changes. Normalize both vectors and check that their dot product matches cosine within floating-point tolerance.

**Record:** One original vector, its scaled version, both raw dot products, both cosine scores, and the normalized dot product. These are constructed numbers, not model quality measurements.

## Example 2 · Sentence pairs and negation

**Predict:** The anchor is “I forgot my password and cannot sign in.” Compare its paraphrase, an invoice question, and the negated statement “I did not forget my password and I can sign in.” Rank the pairs from most to least similar before comparing their scores.

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example pairs
```

**Observe:** Inspect the printed embedding dimension, matrix shape, vector norms, and pair scores. The short NumPy example in the [chapter](../curriculum/03-embeddings.md#6-generate-and-inspect-real-embeddings) shows how to calculate the norms yourself. Two sentences can remain close while disagreeing about a policy. Read their meaning alongside the score; there is no universal passing threshold for this exercise.

**Change:** In a scratch copy of the pair example, change one sentence while preserving its topic: change “can” to “cannot,” swap a date, or replace a number. Rerun with the same model. Then make an unrelated-topic substitution and compare the size of the changes.

**Record:** Original text, modified text, cosine before/after, dimension, and a sentence explaining whether similarity tracked the distinction you cared about.

## Example 3 · Keyword versus semantic search

**Predict:** Choose a development query and identify its relevant document from the labels. Predict which method will retrieve it earlier.

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example search \
  --query "I forgot my password. How can I sign in again?" --top-k 3
```

**Observe:** Compare the ranked document IDs and printed excerpts, then read the complete source text in `data/support_docs.json`. The keyword baseline measures token-set overlap; it is not BM25 or a complete production lexical search engine. A win against this baseline establishes only a win against this baseline on the queries you measured.

**Change:** Rewrite the query as a paraphrase without changing the answer. Next try an exact error code or distinctive phrase copied from a source article. Keep corpus, model, and *k* fixed. Neither method has to win every case.

**Record:** Query, relevant IDs, each method's top-three IDs, first relevant rank, score, and timing reported by the program. Do not compare numerical score magnitudes across different scoring methods as if they had the same scale.

## Example 4 · Find what truncation removed

**Predict:** The example joins all 24 support articles into one handbook. Its final article, `doc-24`, says that each support-ticket attachment may be at most 20 MB. Predict whether a single embedding will receive that part of the text.

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example chunking
```

**Observe:** The query asks for the maximum attachment size in a support ticket. Compare token counts with the runtime model limit, then compare the whole-handbook representation with paragraph chunks. Locate the answer in the original text and inspect the retrieved chunk and its source ID. A long input can be accepted successfully while its tail is silently absent from the model's input.

The retained-tail probe tokenizes the prepared text directly and is scoped to the default model, which adds no document prompt. With a different model, include its prompt and task-specific preprocessing before treating the displayed prefix as the actual encoder input.

**Change:** In a scratch copy, move the answer-bearing paragraph to the beginning while keeping its wording unchanged. Rerun. Then restore its location and compare the existing paragraph chunks with a version that groups two adjacent paragraphs per chunk. Change only one variable in each comparison.

**Record:** Input token count, model limit, chunk count, answer location, top retrieved chunk, and similarity score. Treat the lab's chunking strategy as a controlled experiment; realistic documents may need heading, paragraph, table, or parent-child boundaries.

## Example 5 · Evaluate a configuration

**Predict:** Inspect the development labels and identify at least one query you expect to challenge each method. Do not tune on test queries.

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example evaluate --split dev --top-k 3
```

**Observe:** Read per-query results before the averages. The report computes macro Recall@k and MRR@k over answerable queries. No-answer probes are reported separately, because an empty relevant set has no recall denominator.

**Change:** Compare *k* = 1 and *k* = 3 on development data. For a second embedding configuration, change one meaningful property, such as the document text preparation in a scratch copy or a compatible alternative model selected from its model card. Merely changing *k* is a retrieval configuration comparison, not evidence that the embedding representation improved.

Choose one configuration and write down the choice before running the test split. Carry its model, revision, and text preparation into the test command; this example shows the default configuration:

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example evaluate --split test --top-k 3
```

**Record:** Development and test results separately, with *k*, model/revision, text-preparation description, number of answerable queries, and no-answer observations. Report ties and regressions as well as improvements. A higher average can hide an important exact-identifier failure.

Run all five examples together when you want a repeatable demonstration:

```bash
python builds/03-embeddings-lab/embeddings_lab.py --example all --split dev --top-k 3
```

## Build tasks

- [ ] Run all five examples and save your predictions and observations.
- [ ] Verify dataset structure, IDs, references, and split overlap with `--check`.
- [ ] Create a results note with the configuration fields and tables below.
- [ ] Compare two embedding configurations against the same keyword baseline on development queries.
- [ ] Keep test queries untouched while choosing a configuration, then report the frozen choice's test metrics.
- [ ] Investigate three failures or limitations: one missing-answer query, one wording/identifier/negation case, and one text-preparation case.
- [ ] Explain the relevant source evidence for each investigation; a screenshot of a score is insufficient.
- [ ] Extend the existing 24-document corpus only if your experiment needs it; keep the final collection between 20 and 50 documents, update labels, and record dataset changes.
- [ ] Describe how you would handle an edited document and a model revision change in a persistent index.

## What to record

Keep one results note for this lab. Record Python and package versions, model name/revision, vector dimension, normalization, input template, chunking policy, dataset version, split, *k*, and device. Search prints document-encoding duration; model loading is timed separately. Evaluation prints separate document-encoding, answerable-query encoding, and scoring durations in seconds. The latter timings exclude model loading and no-answer probes. Keep these phases separate and repeat comparable runs at least three times before reporting medians.

| Configuration | Split | Answerable queries | k | Mean Recall@k | MRR@k | Vector dimensions |
|---|---|---:|---:|---:|---:|---:|
| Keyword baseline | dev | | 3 | | | n/a |
| Embeddings A | dev | | 3 | | | |
| Embeddings B | dev | | 3 | | | |
| Frozen choice | test | | 3 | | | |

| Configuration | Split | Median document encoding s | Median query encoding s | Median scoring s |
|---|---|---:|---:|---:|
| Keyword baseline | dev | n/a | n/a | |
| Embeddings A | dev | | | |
| Embeddings B | dev | | | |

Query encoding and scoring cover all answerable queries in the selected split, not one request. Compare the same query count and hardware when interpreting these timings.

| Probe | Expected evidence | Returned ID/chunk | Top score | What failed or remained uncertain | Next controlled change |
|---|---|---|---:|---|---|
| No answer in corpus | none | | | | |
| Identifier/negation | | | | | |
| Truncation/chunking | | | | | |

For local inference, report hosted API calls as **0**. Do not convert that into a claim of zero compute or storage cost. You are measuring retrieval, not the correctness of a generated answer.

## Acceptance

You are done when:

- [ ] `--check` passes and all five examples execute successfully in the documented environment.
- [ ] The geometry exercise demonstrates raw dot-product/cosine differences and normalized equivalence.
- [ ] Your real-model results record finite scores, dimensions, and normalization behavior.
- [ ] You have development metrics for two embedding configurations and the lexical baseline, plus held-out metrics for the frozen choice.
- [ ] You can calculate Recall@k and reciprocal rank manually for one query and match the program's result.
- [ ] Your note includes three investigated failures or limitations and separates no-answer probes from Recall@k/MRR@k.
- [ ] You can state which configuration you would investigate next, with a measured reason and an unresolved limitation.

There is no universal minimum score for this small teaching corpus. Do not edit labels to make an implementation pass or claim production readiness from these checks.

## Teardown

Each example is a foreground Python process that exits when finished; no server or container remains running. If a run is still active, stop it with `Ctrl-C`. Leave the environment with:

```bash
deactivate
```

Keep your results note. The dedicated environment remains in `builds/03-embeddings-lab/.venv`, and downloaded model files remain in the Hugging Face cache for reuse. If reclaiming disk later, remove only this lab's environment or the specific cached model revision after checking that another project does not need it. Do not delete the repository's documentation environment or the entire shared model cache as routine teardown.

Continue to [Module 3 · Retrieval, RAG & Memory](../curriculum/03-rag-memory.md) to add indexing, hybrid retrieval, reranking, and grounded generation around the embedding operation.
