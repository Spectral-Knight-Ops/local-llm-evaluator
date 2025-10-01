import os
import ollama
import json
from datetime import datetime


def run_evaluation(model_list, test_prompts, output_dir=None):
    # Set default output directory (project root / results)
    if output_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(base_dir, "results")

    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamp here, inside function scope
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = os.path.join(output_dir, f"eval_results_{timestamp}.html")

    # Load prompts
    with open(prompts_file, "r") as f:
        evals = json.load(f)

    # Build HTML header
    html_header = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>LLM Eval Results</title>
<style>
  body{{font-family:Segue UI, Roboto, Arial; padding:20px; line-height:1.5; background:#0f1720; color:#e6eef6;}}
  .model{{font-size:1.1rem; font-weight:700; margin-top:1.2rem; color:#f8f9fb;}}
  .task{{margin-top:.6rem; padding:.6rem; border-radius:8px; background:#0b1220;}}
  .prompt{{color:#7bd1ff; font-weight:600;}}
  .output{{background:#08101a; padding:8px; border-radius:6px; margin-top:6px; white-space:pre-wrap; font-family:Menlo, Consolas, monospace; color:#d7e8ff;}}
  .meta{{color:#98a0b0; font-size:.9rem;}}
</style>
</head>
<body>
<h1>LLM Eval Results</h1>
<p class="meta">Generated: {timestamp}</p>
<hr/>
"""

    html_footer = """
</body>
</html>
"""

    # Write results
    with open(outfile, "w") as out:
        out.write(html_header)
        for model in models:
            out.write(f'<div class="model">=== Evaluating {model} ===</div>\n')
            for test in evals:
                response = ollama.chat(model=model, messages=[{"role": "user", "content": test["prompt"]}])
                output = response["message"]["content"]
                out.write('<div class="task">')
                out.write(f'<div class="meta">Task: {test.get("task","")}</div>')
                out.write(f'<div class="prompt">Prompt: {test["prompt"]}</div>')
                out.write(f'<div class="output">{output}</div>')
                out.write('</div>\n')
        out.write(html_footer)

    print(f"Evaluation results saved to {outfile}")
    return outfile

if __name__ == "__main__":
    # Declare models HERE so they’re in scope when running as a script
    #models = ["llava-llama3:latest"]  # or multiple models option below
    models = ["llava-llama3:latest", "codellama:latest"]
    prompts_file = os.path.join(os.path.dirname(__file__), "eval_prompts.json")

    run_evaluation(models, prompts_file)