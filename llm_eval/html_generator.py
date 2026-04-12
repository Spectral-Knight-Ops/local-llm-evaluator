from datetime import datetime


def generate_html_header(timestamp):
    """Generate the HTML header for the evaluation report"""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>LLM Eval Results</title>
<style>
  body {{
    font-family: Segoe UI, Roboto, Arial;
    padding: 20px 20px 20px 280px;
    line-height: 1.5;
    background: #0f1720;
    color: #e6eef6;
  }}
  #sidebar {{
    position: fixed;
    top: 0;
    left: 0;
    width: 260px;
    height: 100vh;
    background: #0b1220;
    overflow-y: auto;
    padding: 16px 12px;
    box-sizing: border-box;
    border-right: 1px solid #1e2d40;
  }}
  #sidebar h2 {{
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #94a3b8;
    margin: 0 0 12px 0;
  }}
  details {{ margin-bottom: 8px; }}
  summary {{
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 600;
    color: #7bd1ff;
    padding: 4px 6px;
    border-radius: 4px;
    list-style: none;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  summary::-webkit-details-marker {{ display: none; }}
  summary::before {{
    content: '▶';
    font-size: 0.65rem;
    transition: transform 0.2s;
  }}
  details[open] summary::before {{ transform: rotate(90deg); }}
  summary:hover {{ background: #0f1a2e; }}
  .sidebar-prompt {{
    display: block;
    font-size: 0.78rem;
    color: #94a3b8;
    padding: 3px 6px 3px 18px;
    border-radius: 4px;
    text-decoration: none;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}
  .sidebar-prompt:hover {{ background: #0f1a2e; color: #e6eef6; }}
  .model {{ font-size: 1.1rem; font-weight: 700; margin-top: 1.2rem; color: #f8f9fb; }}
  .task {{ margin-top: .6rem; padding: .6rem; border-radius: 8px; background: #0b1220; }}
  .prompt {{ color: #7bd1ff; font-weight: 600; }}
  .output {{
    background: #08101a;
    padding: 8px;
    border-radius: 6px;
    margin-top: 6px;
    white-space: pre-wrap;
    font-family: Menlo, Consolas, monospace;
    color: #d7e8ff;
  }}
  .meta {{ color: #98a0b0; font-size: .9rem; }}
  .metrics {{ margin: 8px 0; padding: 8px; background: #0a1420; border-radius: 4px; font-size: 0.85rem; }}
  .metric {{ margin-right: 15px; color: #94a3b8; }}
</style>
</head>
<body>
<nav id="sidebar">
  <h2>Navigation</h2>
  <div id="sidebar-content"></div>
</nav>
<h1>LLM Eval Results</h1>
<p class="meta">Generated: {timestamp}</p>
<hr/>
"""


def generate_html_footer():
    """Generate the HTML footer for the evaluation report"""
    return """
<script>
document.addEventListener('DOMContentLoaded', function() {
  const sidebar = document.getElementById('sidebar-content');
  const modelDivs = document.querySelectorAll('.model');

  modelDivs.forEach(function(modelDiv, modelIndex) {
    modelDiv.id = 'model-' + modelIndex;
    const modelName = modelDiv.textContent
      .replace(/^=+\\s*Evaluating\\s*/i, '')
      .replace(/\\s*=+$/, '')
      .trim();

    const tasks = [];
    let sibling = modelDiv.nextElementSibling;
    while (sibling && !sibling.classList.contains('model')) {
      if (sibling.classList.contains('task')) tasks.push(sibling);
      sibling = sibling.nextElementSibling;
    }

    tasks.forEach(function(task, taskIndex) {
      task.id = 'task-' + modelIndex + '-' + taskIndex;
    });

    const details = document.createElement('details');
    details.open = true;
    const summary = document.createElement('summary');
    summary.textContent = modelName;
    details.appendChild(summary);

    tasks.forEach(function(task, taskIndex) {
      const promptEl = task.querySelector('.prompt');
      const promptText = promptEl
        ? promptEl.textContent.replace(/^Prompt:\\s*/i, '').trim()
        : 'Prompt ' + (taskIndex + 1);

      const link = document.createElement('a');
      link.href = '#' + task.id;
      link.className = 'sidebar-prompt';
      link.title = promptText;
      link.textContent = promptText;
      details.appendChild(link);
    });

    sidebar.appendChild(details);
  });
});
</script>
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
