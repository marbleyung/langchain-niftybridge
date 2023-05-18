from fastapi import FastAPI
from models import Prompt
from main import get_answer

app = FastAPI()

@app.get('/api/send/')
def create_query(query: Prompt):
    return "Ask me something"


@app.post('/api/send/')
def create_query(query: Prompt):
    answer = get_answer(query=str(query))
    return answer
