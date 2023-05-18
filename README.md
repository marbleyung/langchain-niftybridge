# langchain-niftybridge
This API service allows you to ask any questions realted to NiftyBridge.pdf to OpenAI LLM. It also allows you to do the same with any other PDF's.
Here is some instructions. Instructions in " " means commands which you should run in terminal
_
On Windows
1. Win+R -> "cmd" -> enter
2. "cd {directory/name}" (go to directory where you want to base the service)
3. "git clone https://github.com/marbleyung/langchain-niftybridge.git"
4. "cd langchain-niftybridge"
5. "python -m venv venv"
6. "cd venv/Scripts"
7. 'activate'
8. "cd .." (run it twice)
9. "pip install -r req.txt"
10. "type > .env", enter

11. in .env file, create next lines:
OPENAI_API_KEY=sk-YOURSECRETKEY
OPENAI_API_TYPE=open_ai
_
If you DON'T want to use a docker:
12. "uvicorn api:app --reload"

If you WANT to use a docker:
12. "docker build -t niftybridge ."
12.1 "docker run niftybridge"
_

13. In your browser, open "http://127.0.0.1:8000/docs"
14. You will find line starts with "POST", press on it
15. Under the arrow (in "Parameters" line) press "Try it out"
16. In "Request body" field change "string" to your question to NiftyBridge AI. 
(example: "query": "string" -> "query": "What is NiftyBridge?")
17. Press "execute" and get an answer
