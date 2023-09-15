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


def get_chatbot_response(chatbot_response):
    return extract_phone_numbers(chatbot_response['result'].strip())
    # print(extract_phone_numbers(chatbot_response['result'].strip()))
    # print('\n문서 출처:')
    # for source in chatbot_response["source_documents"]:
    #     print(source.metadata['source'])

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


# 텍스트 파일 로드 (학습해야할 내용)
loader = DirectoryLoader('./backend/ktdata', glob="*.txt", loader_cls=TextLoader,loader_kwargs={"encoding": "utf-8"})
documents = loader.load()

# print('문서의 개수 :', len(documents)

# 텍스트 분리 Split texts
text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

print('분할된 텍스트의 개수 :', len(texts))

# source_lst = []
# for i in range(0, len(texts)):
#   source_lst.append(texts[i].metadata['source'])

# element_counts = Counter(source_lst)
# filtered_counts = {key: value for key, value in element_counts.items() if value >= 2}
# print('2개 이상으로 분할된 문서 :', filtered_counts)
# print('분할된 텍스트의 개수 :', len(documents) + len(filtered_counts))

#크로마 DB생성
embedding = OpenAIEmbeddings()

vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embedding)


#검색기능
# retriever = vectordb.as_retriever()
# retriever_txt = "검색할내용 입력"
# docs = retriever.get_relevant_documents(retriever_txt)
# print('유사 문서 개수 :', len(docs))
# print('--' * 20)
# print('첫번째 유사 문서 :', docs[0])
# print('--' * 20)
# print('각 유사 문서의 문서 출처 :')
# for doc in docs:
#     print(doc.metadata["source"])

#K개 만큼 반환
retriever = vectordb.as_retriever(search_kwargs={"k": 4})

# docs = retriever.get_relevant_documents("검색어 입력?") # 찐 검색어

# for doc in docs:
#     print(doc.metadata["source"])

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True)



# #Test1
# input_text = "5G심플 요금제를 Python 코드로 html 표를 작성하는 소스짜줘"
# chatbot_response = qa_chain(input_text)
# get_chatbot_response(chatbot_response)
# lineFeed()


# #Test2
# input_text = "5G심플 70GB 데이터는 몇이고, 음성은 몇분이야?"
# chatbot_response = qa_chain(input_text)
# get_chatbot_response(chatbot_response)
# lineFeed()

# #Test3
# input_text = "5G심플 110GB 쓸껀데 스마트기기 공유데이터는 몇이야?"
# chatbot_response = qa_chain(input_text)
# get_chatbot_response(chatbot_response)
# lineFeed()

# #Test4
# input_text = "용돈이 6만6천원인데 휴대폰 요금제 쓸만한거 추천해줄래?"
# chatbot_response = qa_chain(input_text)
# get_chatbot_response(chatbot_response)
# lineFeed()


print("모델과 대화를 시작합니다. 종료하려면 '종료'라고 입력하세요.")
while True:
    user_content = input("사용자 : ")

    if user_content=='종료':
        print('종료 되었습니다.')
        break
    
    chatbot_response = qa_chain(user_content)
    print(f"GPT : {get_chatbot_response(chatbot_response)}")
    lineFeed()