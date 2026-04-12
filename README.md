========== Features ==========

    Evaluate one or more local LLMs against structured prompts
    
    Output neatly formatted HTML reports with prompts, outputs, and metrics
    
    Quickly change models and prompts to suit your personal needs


========== Usage ==========

Pre-Requisites

    Install Docker: https://www.docker.com/products/docker-desktop
    Install Ollama: https://ollama.com/download
    Download the models you want to test: https://ollama.com/search

    If this is your first time working with local LLMs, I strongly suggest you do some research on 
    hardware constraints in regard to choosing a local llm. For proof of concept for this repo, 
    install the needed models: llava-llama3:latest, codellama:latest

How do I change the prompts being tested?

    Edit eval_prompts.json
    
    The "task" field is just metadata and can be labeled however you'd like
    The "prompt" field is what will be sent to the LLM

How do I use the tool?

    # 1. Clone the repository
    git clone https://github.com/Spectral-Knight-Ops/local-llm-evaluator.git
    cd local-llm-evaluator

    # 2. Run the evaluator
    docker compose run llm-evaluator

How do I view the results?

    A /results/ directory will populate in the project root
    A timestamped HTML file will appear in this directory
    Ex: eval_results_<date>_<time>.html

    Open this file in your browser to view the formatted results

Future goals for this tool:

    # 1. Publish a prebuilt image to Docker Hub to eliminate the local build step


========== License ==========

    This project is licensed under the MIT License – see the LICENSE file for details.


========== Contributing ==========
    
    Contributions are welcome!
