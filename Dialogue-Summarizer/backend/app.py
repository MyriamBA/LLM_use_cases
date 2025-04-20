from fastapi import FastAPI
from pydantic import BaseModel
from model import summarize

app = FastAPI()

class DialogueInput(BaseModel):
    dialogue: str

@app.post("/summarize")
def summarize_dialogue(input_data: DialogueInput):
    summary = summarize(input_data.dialogue)
    return {"summary": summary}


