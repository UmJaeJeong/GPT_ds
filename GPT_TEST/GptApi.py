import os
import openai

#환경설정에 등록된 key값 
# openai.api_key = os.getenv("OPENAI_API_KEY")

#Chat-GPT4로 했을때 채팅이 가능하고 / GPT3는 채팅이 불가능핟 그래서 히스토리를 사용행야함
openai.api_key = "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"


def chat_with_model(message):
    response = openai.Completion.create(
        model="curie:ft-personal-2023-06-23-02-11-24",
        prompt=message,
        temperature=0.2,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# 대화 시작
print("모델과 대화를 시작합니다. 종료하려면 '종료'라고 입력하세요.")
messages = []
while True:
    user_content = input("사용자 : ")
    messages.append({"role": "user", "content": f"{user_content}"})    

    if user_content == "종료":
        break
    
    # 사용자 입력을 모델에 전달하여 응답 받기
    assistant_content = str(chat_with_model(user_content)).split('\n')[0]

    
    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")
######################################################################################################3

# messages = []
# while True:
#     user_content = input("사용자 : ")
#     messages.append({"role": "user", "content": f"{user_content}"})

#     # completion = openai.ChatCompletion.create(model="curie:ft-personal-2023-06-22-08-52-09", messages=messages)

#     completion = openai.Completion.create(engine="curie:ft-personal-2023-06-22-08-52-09", messages=messages)


#     assistant_content = completion.choices[0].message["content"].strip()

#     messages.append({"role": "assistant", "content": f"{assistant_content}"})

#     print(f"GPT : {assistant_content}")


# def chat_with_gpt3(prompt):
#     response = openai.Completion.create(
#         engine="curie:ft-personal-2023-06-23-02-11-24",
#         prompt=prompt,
#         max_tokens=50,
#         temperature=1.0,
#         n=1,
#         stop=None
#     )
#     if response and response.choices:
#         return response.choices[0].text.strip()
#     return None

# print("AI: 안녕하세요! 대화를 시작해봅시다.")
# while True:
#     user_input = input("사용자: ")

#     if user_input.lower() in ['exit', 'quit', 'bye']:
#         print("AI: 채팅을 종료합니다.")
#         break

#     prompt = f"User: {user_input}\nAI:"
#     response = chat_with_gpt3(prompt)
#     print("AI:", response)


######################################################################################################3

# messages = []
# while True:
#     user_content = input("사용자 : ")
#     messages.append({"role": "user", "content": f"{user_content}"})

#     # completion = openai.ChatCompletion.create(model="curie:ft-personal-2023-06-22-08-52-09", messages=messages)

#     completion = openai.Completion.create(engine="curie:ft-personal-2023-06-22-08-52-09", messages=messages)


#     assistant_content = completion.choices[0].message["content"].strip()

#     messages.append({"role": "assistant", "content": f"{assistant_content}"})

#     print(f"GPT : {assistant_content}")


