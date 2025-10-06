from datetime import datetime


def generate_html_header(timestamp):
    """Generate the HTML header for the evaluation report"""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>LLM Eval Results</title>
<style>
  body{{font-family:Segoe UI, Roboto, Arial; padding:20px; line-height:1.5; background:#0f1720; color:#e6eef6;}}
  .model{{font-size:1.1rem; font-weight:700; margin-top:1.2rem; color:#f8f9fb;}}
  .task{{margin-top:.6rem; padding:.6rem; border-radius:8px; background:#0b1220;}}
  .prompt{{color:#7bd1ff; font-weight:600;}}
  .output{{background:#08101a; padding:8px; border-radius:6px; margin-top:6px; white-space:pre-wrap; font-family:Menlo, Consolas, monospace; color:#d7e8ff;}}
  .meta{{color:#98a0b0; font-size:.9rem;}}
  .metrics{{margin:8px 0; padding:8px; background:#0a1420; border-radius:4px; font-size:0.85rem;}}
  .metric{{margin-right:15px; color:#94a3b8;}}
</style>
</head>
<body>
<h1>LLM Eval Results</h1>
<p class="meta">Generated: {timestamp}</p>
<hr/>
"""


def generate_html_footer():
    """Generate the HTML footer for the evaluation report"""
    return """
</body>
</html>
"""


def generate_task_html(test, output, metrics=None):
    """Generate HTML for a single task and its output"""
    html = '<div class="task">'
    html += f'<div class="meta">Task: {test.get("task", "")}</div>'
    html += f'<div class="prompt">Prompt: {test["prompt"]}</div>'
    
    if metrics:
        html += '<div class="metrics">'
        html += f'<span class="metric">⏱️ Duration: {metrics["eval_duration"]:.2f}s</span>'
        html += f'<span class="metric">🔤 Tokens/s: {metrics["tokens_per_second"]:.1f}</span>'
        html += f'<span class="metric">📊 Total tokens: {metrics["total_tokens"]}</span>'
        html += '</div>'
    
    html += f'<div class="output">{output}</div>'
    html += '</div>\n'
    return html