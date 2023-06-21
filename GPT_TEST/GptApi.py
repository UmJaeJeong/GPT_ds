import os
import openai

#아래의 커맨드 입력후 openai 사용 가능
#pip install openai 


#환경설정에 등록된 key값 
# openai.api_key = os.getenv("OPENAI_API_KEY")

#OPENAI_API_KEY는 발급받아서 사용
openai.api_key = "OPENAI_API_KEY"

#대화 메시지 저장으로 기존 데이터 보유
messages = []
while True:
    user_content = input("사용자 : ")

    messages.append({"role": "user", "content": f"{user_content}"})

    #text-davinci-003
    #gpt-3.5-turbo
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
  

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")


