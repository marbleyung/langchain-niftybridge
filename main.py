import tiktoken
from dotenv import load_dotenv
from os import getenv

from langchain import FAISS, OpenAI, PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter


load_dotenv()
OPENAI_API_KEY = getenv('OPENAI_API_KEY')
PROMPT_TOKEN_LIMIT = 2048
PDF_NAME = 'NiftyBridge.pdf'


def convert_pdf(pdf: str) -> list['Document']:
    return PyPDFLoader(pdf).load()


def split_text_to_chunks(document: list['Document']) -> list['Document']:
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(document)
    return chunks


def add_text_to_db(chunks: list['Document']):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    return db


def create_prompt_template():
    message = """Start your answer with 'Hello! I'm NiftyBridge AI assistant.\n'
    Use the following pieces of context to answer the question at the end.
    If you don't know the answer, say 
    'I don't know, please contact with support by email support@nifty-bridge.com'
    {context}
    Question: {question}
    Helpful Answer:
    """

    prompt_template = PromptTemplate.from_template\
        (template=message)
    return prompt_template


def create_chain(db: FAISS, prompt_template: PromptTemplate) -> RetrievalQA:
    retriever = db.as_retriever(search_type='similarity',
                                search_kwargs={'k': 2})
    chain = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type='stuff',
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={
            'prompt': prompt_template
        }
    )
    return chain


def check_prompt_length(query: str, encoding_name='cl100k_base') -> bool:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(query))
    return num_tokens < PROMPT_TOKEN_LIMIT


def answer_to_prompt(query: str, chain: RetrievalQA):
    answer = chain({'query': query})
    return answer


def get_answer(query, pdf=PDF_NAME, *args, **kwargs):
    document = convert_pdf(pdf=pdf)
    print('Document converted')
    
    chunks = split_text_to_chunks(document=document)
    print('Document spliced into chunks')
    
    db = add_text_to_db(chunks=chunks)
    print('DB has been created')
    
    prompt_template = create_prompt_template()
    chain = create_chain(db=db,
                         prompt_template=prompt_template)
    print('Chain has been initialized')

    if check_prompt_length(query):
        answer = answer_to_prompt(query, chain=chain)
        result = answer['result'].strip()
        return result
    else:
        raise ValueError('Prompt is too long')



