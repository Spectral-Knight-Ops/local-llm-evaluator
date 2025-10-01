========== Features ==========

    Evaluate one or more local LLMs against structured prompts
    
    Output neatly formatted HTML reports with prompts and outputs
    
    Quickly change models and prompts to suit your personal needs
    
    Simple Python package structure


========== Usage ==========

Pre-Requisites
 
    Install ollama here: https://ollama.com/download
    Download the models you want to test here: https://ollama.com/search

    If this is your first time working with local LLMs, I strongly suggest you do some research on hardware
    constraints in regard to choosing a local llm. For proof of concept for this repo, install the
    needed models: llava-llama3:latest, codellama:latest

How do I change the models being tested?
    
    In evaluator.py, locate the list declaring the models near the end:
    models = ["llava-llama3:latest", "codellama:latest"]

    Replace the list with the models you want to use

How do I change the prompts being tested?

    Edit eval_prompts.json
    
    The "task" field is just metadata and can be labeled however you'd like
    The "prompt" field is what will be sent to the LLM

How do I run the tool?

    # 1. Clone the repository
    git clone https://github.com/Spectral-Knight-Ops/llm_eval_tool.git
    cd llm_eval_tool.git

    # 2. Create and activate a virtual environment
    python -m venv .venv
    # On Linux/MacOS
    source .venv/bin/activate
    # On Windows (PowerShell)
    .venv\Scripts\activate

    # 3. Install dependencies
    pip install -r requirements.txt

    # 4. Run the evaluator
    python -m llm_eval.evaluator

How do I view the results?

    A /results/ directory will populate in the project root
    A timestamped HTML file will appear in this directory
    Ex: eval_results_<date>_<time>.html

    Open this file in your browser to view the formatted results


Future goal(s) for this tool:

    # 1. Add CLI interface for --models, --prompts, --output

========== License ==========

    This project is licensed under the MIT License – see the LICENSE file for details.

========== Contributing ==========
    
    Contributions are welcome!