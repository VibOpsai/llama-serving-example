"""Llama 3 inference server — minimal vLLM wrapper."""

from vllm import LLM, SamplingParams
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Llama Serving")
llm = LLM(model="meta-llama/Meta-Llama-3-8B-Instruct", tensor_parallel_size=2)


class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = 0.7


@app.post("/v1/completions")
def complete(req: CompletionRequest):
    params = SamplingParams(max_tokens=req.max_tokens, temperature=req.temperature)
    outputs = llm.generate([req.prompt], params)
    return {"text": outputs[0].outputs[0].text}


@app.get("/health")
def health():
    return {"status": "ok"}
