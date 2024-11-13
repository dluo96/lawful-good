# Lawful Good

## Get Started
Clone the repo:
```bash
git clone git@github.com:dluo96/lawful-good.git
```


Install the `inspect_ai` and `inspect_evals` Python packages:
```bash
pip install inspect_ai
pip install git+https://github.com/UKGovernmentBEIS/inspect_evals
```

Install the package locally
```bash
cd lawful-good
pip install -e .
```


### Example Evaluation with Ollama
- Install [ollama](https://ollama.com/download). On Linux, simply run
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
- Run (say) Llama2 3B:
    ```
    ollama run llama3.2
    ```
    This will automatically pull (download) Llama2 3B for you and then run.
- To run Inspect evals with Ollama, you will need to install the `openai` package:
    ```
    pip install openai
    ```
- Run the example evaluation script:
    ```bash
    inspect eval lg/lawful_good.py --model ollama/llama3.2
    ```
- NOTE: if you receive the error `PermissionError: [Errno 13] Permission denied: '/run/user/1000'`, try setting the following environment variable:
    ```bash
    export XDG_RUNTIME_DIR=/tmp
    ```
    and re-running. 
