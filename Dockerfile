FROM python:3.9-bullseye
WORKDIR /fastapiapp
COPY ./ ./fastapiapp
RUN pip install -r fastapiapp/req.txt
ENV FASTAPI_APP=api.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
EXPOSE 8000
CMD [ "uvicorn", "fastapiapp.api:app", "--reload", "--host", "0.0.0.0"]