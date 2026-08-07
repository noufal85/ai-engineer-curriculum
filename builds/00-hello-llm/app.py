"""Build 00 — hello-llm.

The smallest useful LLM service: one streaming endpoint and one
schema-validated extraction endpoint. Everything later in the curriculum is a
variation on these two moves — stream tokens to a user, and turn free text into
a validated object.

Run it with `docker compose up` (see README). Needs ANTHROPIC_API_KEY.
"""

import os

import anthropic
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel

# The model is a knob, not a constant: Opus for quality, Haiku for cheap
# iteration while you're learning. Override with MODEL in your .env.
MODEL = os.environ.get("MODEL", "claude-opus-4-8")

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
app = FastAPI(title="hello-llm")


class ChatIn(BaseModel):
    message: str


class ExtractIn(BaseModel):
    text: str


class Analysis(BaseModel):
    """The shape we force the model's output into. This IS the contract —
    the model must return exactly these fields, validated before we trust it."""

    sentiment: str  # "positive" | "neutral" | "negative"
    topics: list[str]
    summary: str
    action_required: bool


@app.get("/health")
def health() -> dict:
    return {"ok": True, "model": MODEL}


@app.post("/chat")
def chat(body: ChatIn) -> StreamingResponse:
    """Stream the model's answer token-by-token. Streaming is the whole reason
    chat UIs feel fast — you show the first token in ~1s instead of waiting for
    the full response."""

    def tokens():
        with client.messages.stream(
            model=MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": body.message}],
        ) as stream:
            for text in stream.text_stream:
                yield text

    return StreamingResponse(tokens(), media_type="text/plain")


@app.post("/extract")
def extract(body: ExtractIn) -> Analysis:
    """Turn free text into a validated Analysis object. `messages.parse` +
    a Pydantic schema is the reliable way to get structured data out of an LLM —
    the model is constrained to the schema, and the SDK validates it."""
    resp = client.messages.parse(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Analyze this text:\n\n{body.text}"}],
        output_format=Analysis,
    )
    return resp.parsed_output


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """A tiny page so `docker compose up` → open localhost:8000 shows something
    you can actually poke at."""
    return """
<!doctype html><meta charset=utf-8><title>hello-llm</title>
<style>body{font:16px system-ui;max-width:44rem;margin:3rem auto;padding:0 1rem}
textarea{width:100%;height:5rem}pre{white-space:pre-wrap;background:#f4f4f5;padding:1rem;border-radius:8px}
button{padding:.5rem 1rem;margin:.5rem 0}</style>
<h1>hello-llm</h1>
<h2>1 · Streaming chat</h2>
<textarea id=msg>Explain what an embedding is, in two sentences.</textarea>
<button onclick=chat()>Stream</button>
<pre id=out></pre>
<h2>2 · Schema-validated extraction</h2>
<textarea id=txt>The new dashboard is fast but the login page keeps timing out and support hasn't replied in 3 days.</textarea>
<button onclick=extract()>Extract</button>
<pre id=ext></pre>
<script>
async function chat(){
  const out=document.getElementById('out');out.textContent='';
  const r=await fetch('/chat',{method:'POST',headers:{'content-type':'application/json'},
    body:JSON.stringify({message:document.getElementById('msg').value})});
  const rd=r.body.getReader(),dec=new TextDecoder();
  for(;;){const{value,done}=await rd.read();if(done)break;out.textContent+=dec.decode(value)}
}
async function extract(){
  const ext=document.getElementById('ext');ext.textContent='…';
  const r=await fetch('/extract',{method:'POST',headers:{'content-type':'application/json'},
    body:JSON.stringify({text:document.getElementById('txt').value})});
  ext.textContent=JSON.stringify(await r.json(),null,2);
}
</script>
"""
