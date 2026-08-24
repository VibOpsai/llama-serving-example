# llama-serving-example

Minimal Llama 3 8B inference server using vLLM. Deploy on GPU with one command via [VibOps](https://vibops.ai).

## Quick start

```bash
# With VibOps — one conversation
"Clone this repo and deploy it on my GPU cluster"
```

## Manual

```bash
docker build -t llama-serving .
docker run --gpus 2 -p 8000:8000 llama-serving
curl -X POST http://localhost:8000/v1/completions \
  -d '{"prompt": "Explain GPU inference", "max_tokens": 100}'
```

## Files

| File | Description |
|------|-------------|
| `serve.py` | FastAPI + vLLM inference server |
| `Dockerfile` | Container image (based on vllm-openai) |
| `requirements.txt` | Python dependencies |
