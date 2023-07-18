import openai
import re

#환경설정에 등록된 key값 
# openai.api_key = os.getenv("OPENAI_API_KEY")

#Chat-GPT4로 했을때 채팅이 가능하고 / GPT3는 채팅이 불가능핟 그래서 히스토리를 사용행야함

# OpenAI API 인증 설정
openai.api_key = "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"


messages = []
while True:
    user_content = input("사용자 : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")


