# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Prerequisites

- [Ollama](https://ollama.com/download) must be running locally
- Models must be pulled via `ollama pull <model_name>` before evaluation

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Running the Evaluator

```bash
# Interactive model selection, then runs all prompts in eval_prompts.json
python3 -m llm_eval.evaluator

# With full response output in terminal
python3 -m llm_eval.evaluator --trace
```

Results are written to `results/eval_results_<timestamp>.html`.

## Architecture

The tool is a single-pass evaluation pipeline:

1. **`evaluator.py`** — Entry point. Calls `select_models_interactively()`, then iterates over (model × prompt) pairs, timing each `ollama.chat()` call and writing results incrementally to an HTML file.

2. **`utils.py`** — Wraps `ollama.list()` (handles multiple response formats across ollama versions) and provides the interactive numbered-list model selector.

3. **`html_generator.py`** — Produces the HTML report: a dark-themed static file with per-task blocks showing the prompt, metrics (duration, tokens/s, total tokens), and raw model output.

4. **`eval_prompts.json`** — The test suite. Each entry has a `"task"` label (metadata only, not used in filtering) and a `"prompt"` sent verbatim to each model.

Token counts in metrics are word-split estimates, not actual token counts from the ollama API.
