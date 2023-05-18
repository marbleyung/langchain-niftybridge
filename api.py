from fastapi import FastAPI
try:
    from fastapiapp.models import Prompt
    from fastapiapp.main import get_answer
except ModuleNotFoundError:
    from models import Prompt
    from main import get_answer


app = FastAPI()


@app.get('/api/send/')
def create_query():
    return "Ask me something"


@app.post('/api/send/')
def create_query(query: Prompt):
    answer = get_answer(query=str(query))
    return answer
