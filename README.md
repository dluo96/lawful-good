# AgentBench
Benchmark for assessing legal capabilities of LLM agents!

## Get Started
Clone the repo:
```bash
git clone git@github.com:dluo96/agent-bench.git
```

Install:
```bash
cd agent-bench
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

- Run the example evaluation script:
    ```bash
    inspect eval example.py --model ollama/llama3.2
    ```
- NOTE: if you receive the error `PermissionError: [Errno 13] Permission denied: '/run/user/1000'`, try setting the following environment variable:
```bash
export XDG_RUNTIME_DIR=/tmp
```
and re-running. 