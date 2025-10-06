import os
import ollama
import json
import argparse
import time
from datetime import datetime
from .utils import get_available_models, select_models_interactively
from .html_generator import generate_html_header, generate_html_footer, generate_task_html





def run_evaluation(model_list, test_prompts, output_dir=None, trace=False):
    # Set default output directory (project root / results)
    if output_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(base_dir, "results")

    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamp here, inside function scope
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = os.path.join(output_dir, f"eval_results_{timestamp}.html")

    # Load prompts
    with open(test_prompts, "r") as f:
        evals = json.load(f)

    # Generate HTML components
    html_header = generate_html_header(timestamp)
    html_footer = generate_html_footer()

    # Calculate total queries for progress tracking
    total_queries = len(models) * len(evals)
    current_query = 0

    # Write results
    with open(outfile, "w") as out:
        out.write(html_header)
        for model in models:
            out.write(f'<div class="model">=== Evaluating {model} ===</div>\n')
            for test in evals:
                current_query += 1
                percentage = (current_query / total_queries) * 100

                # Print status nicely formatted
                print(f"󱚣 Progress: {percentage:.1f}% | Model: {model}")
                print(f"󱍊 Query: {test['prompt']}")
                print("-" * 80)

                # Time the evaluation
                start_time = time.time()
                response = ollama.chat(
                    model=model, messages=[{"role": "user", "content": test["prompt"]}]
                )
                end_time = time.time()
                
                output = response["message"]["content"]
                eval_duration = end_time - start_time
                
                # Extract token metrics if available
                prompt_tokens = len(test['prompt'].split())  # Rough estimate
                output_tokens = len(output.split())  # Rough estimate
                total_tokens = prompt_tokens + output_tokens
                tokens_per_second = total_tokens / eval_duration if eval_duration > 0 else 0

                if trace:
                    print(f"\nResponse: {output}\n{'=' * 50}")

                # Create metrics dict for HTML generation
                metrics = {
                    'prompt_duration': eval_duration,
                    'eval_duration': eval_duration,
                    'tokens_per_second': tokens_per_second,
                    'prompt_tokens': prompt_tokens,
                    'output_tokens': output_tokens,
                    'total_tokens': total_tokens
                }
                
                out.write(generate_task_html(test, output, metrics))
        out.write(html_footer)

    print(f"Evaluation results saved to {outfile}")
    return outfile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Evaluate local LLMs against test prompts"
    )
    parser.add_argument(
        "--trace", action="store_true", help="Show full output during evaluation"
    )
    args = parser.parse_args()

    prompts_file = os.path.join(os.path.dirname(__file__), "eval_prompts.json")

    # Get models interactively
    models = select_models_interactively()

    if not models:
        print("No models selected. Exiting.")
    else:
        print(f"\nSelected models: {', '.join(models)}")
        print("\n" + "=" * 80)
        run_evaluation(models, prompts_file, trace=args.trace)
