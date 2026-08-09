# Optional Specialization Tracks

These tracks come after the shared core or alongside a capstone. They deepen a specific area without making every learner study every model family or infrastructure path.

## Multimodal and realtime systems

- Vision models, image understanding, document intelligence, OCR, and table extraction.
- Image generation: diffusion models, image-generation APIs, prompt-to-image quality control, and when generation belongs in a product.
- Speech-to-text, text-to-speech, voice and audio generation, audio classification, and realtime interaction.
- Video sampling, temporal context, multimodal RAG, and modality-specific safety.
- Evaluation for transcription quality, visual grounding, latency, and user trust.

Suggested build: a document or meeting assistant that combines text, images, tables, and audio with citations and human correction.

## Model adaptation and open weights

- Prompting versus RAG versus fine-tuning: choose based on the failure mode.
- Dataset curation, synthetic data, supervised fine-tuning, LoRA/QLoRA, PEFT, and evaluation splits.
- Distillation, quantization, model merging, model cards, licensing, and data governance.
- Benchmarking hosted and open-weight models on the same task, cost, latency, and quality measures.

Suggested build: adapt a small model to a constrained extraction or classification task, then compare it with prompting and a larger hosted model.

## Local inference and model serving

- vLLM, llama.cpp, Ollama, and other inference runtimes.
- GPU/VRAM sizing, batching, KV cache behavior, quantization, and autoscaling.
- Privacy, data residency, offline operation, and total cost of ownership.
- Edge and on-device inference: mobile/browser runtimes, model size versus capability, and offline fallbacks.
- Load testing and quality baselines for a self-hosted model.

Suggested build: serve an open-weight model locally, expose an OpenAI-compatible endpoint, and produce a cost/latency/quality report.

## Coding and sandboxed agents

- Repository context, code search, patch generation, test execution, and review loops.
- Sandboxed execution, filesystem boundaries, network policy, and secret isolation.
- Human approval for changes, reproducible environments, and rollback.
- Task-success evals based on real bugs or bounded repository tasks.

Suggested build: a coding agent that fixes a small issue in a fixture repository while running tests inside a restricted sandbox.

## Choosing a specialization

Choose based on the work you want to do next, not on novelty. Each specialization should still produce a measured build, a threat model, an eval suite, and a clear explanation of when the technique is the wrong choice.
