from fastapi import FastAPI
try:
    from fastapiapp.models import Prompt
    from fastapiapp.main import get_answer
except ModuleNotFoundError:
    from models import Prompt
    from main import get_answer


app = FastAPI()


@app.get('/api/send/')
async def create_query():
    return "Ask me something"


@app.post('/api/send/')
<<<<<<< HEAD
async def create_query(query: Prompt):

=======
def create_query(query: Prompt):
>>>>>>> 00025123a726e674b3235ab9176285fd3ea7fd58
    answer = get_answer(query=str(query))
    return answer
