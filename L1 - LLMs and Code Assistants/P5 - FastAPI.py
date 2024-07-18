from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize_text(data: TextData):
    text = data.text
    words = text.split()
    summary = ' '.join(words[:min(100, len(words))])
    return {"summary": summary}

@app.post("/token_count/")
async def token_count(data: TextData):
    text = data.text
    # Count the number of words in the text
    tokens = len(text.split())
    return {"token_count": tokens}