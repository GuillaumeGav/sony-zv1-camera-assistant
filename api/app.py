from fastapi import FastAPI, Query
from zv1_assistant import ask, setup_assistant

app = FastAPI()
# loading the model, index, metadata
index, model, metadata = setup_assistant()

@app.get("/")
def read_root():
    return {" Welcome ":" I am your Sony Zv1 assistant :)"}

@app.get("/ask")
def ask_zv1(question : str):
    return {"zv1_assistant" : ask(question, index, metadata, model)}
