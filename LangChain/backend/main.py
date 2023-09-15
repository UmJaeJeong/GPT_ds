from fastapi import FastAPI
from pydantic import BaseModel
import openai
from typing import List
from bs4 import BeautifulSoup
import requests
import os
import re
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader, TextLoader


api_key = "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"
os.environ["OPENAI_API_KEY"] = api_key

# FastAPI 앱 생성
app = FastAPI()

qa_chain = None
# OpenAI API 키 설정
openai.api_key = "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"

# FastAPI의 startup 이벤트를 사용하여 초기화 함수 등록
@app.on_event("startup")
async def startup_event():
    # 여기에 초기화 작업을 수행할 코드를 작성합니다.
    # 텍스트 파일 로드 (학습해야할 내용)
    loader = DirectoryLoader('./backend/ktdata', glob="*.txt", loader_cls=TextLoader,loader_kwargs={"encoding": "utf-8"})
    documents = loader.load()

    # 텍스트 분리 Split texts
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    print('분할된 텍스트의 개수 :', len(texts))


    #크로마 DB생성
    embedding = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding)


    #K개 만큼 반환
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})


    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True)


def get_chatbot_response(chatbot_response):
    return extract_phone_numbers(chatbot_response['result'].strip())

#기능1 : 스크럼블/마스킹 기능(전화번호)
def extract_phone_numbers(text):
    pattern = re.compile(r'\d+[-]\d+[-]\d+')  # 전화번호 패턴 정규식

    phone_numbers = pattern.findall(text)

    scrumble_phone = '010-xxxx-xxxx'
    for phone in phone_numbers:
        text = text.replace(phone,scrumble_phone)
    return text

#기능2 : 키워드 필터링 기능

#기능3 : 텍스트 로드

#기능4: LineFeed
def lineFeed():
   print("----------------------------------------------------------")





print("모델과 대화를 시작합니다. 종료하려면 '종료'라고 입력하세요.")
while True:
    user_content = input("사용자 : ")

    if user_content=='종료':
        print('종료 되었습니다.')
        break
    
    chatbot_response = qa_chain(user_content)
    print(f"GPT : {get_chatbot_response(chatbot_response)}")
    lineFeed()



class Turn(BaseModel):
    role: str
    content: str
class Messages(BaseModel):
    messages: List[Turn]  # [{"role": "user", "content": "blahblahblah"}, {"role": "assistant", "content": "blahblahblah"}, ...]

@app.post("/chat", response_model=Turn)
def post_chat(messages: Messages):
    messages = messages.dict()
    chatbot_response = qa_chain(messages=messages['messages'])
    print("ChatBot"+chatbot_response)
    return chatbot_response

@app.post("/finetune", response_model=Turn)
def post_chat(messages: Messages):
    messages = messages.dict()
    assistant_turn = chatFineTune(messages=messages['messages'])
    return assistant_turn
