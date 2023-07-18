import openai
import re

# OpenAI API 인증 설정
openai.api_key = "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"


def chat_with_model(message):
    response = openai.Completion.create(
        # model="text-davinci-003",
        # engine="davinci:ft-personal:um2-2023-06-27-08-59-10", #처음 파인튜닝
        engine="davinci:ft-rater:um-krater-up-2023-07-16-13-50-03", #파인튜닝 모델에 한번더 파인튜닝
        prompt=message,
        temperature=0.2,
        max_tokens=256,
        top_p=1, 
        n=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


#스크럼블/마스킹 기능(전화번호)
def extract_phone_numbers(text):
    pattern = re.compile(r'\d+[-]\d+[-]\d+')  # 전화번호 패턴 정규식

    phone_numbers = pattern.findall(text)

    scrumble_phone = '010-xxxx-xxxx'
    for phone in phone_numbers:
        text = text.replace(phone,scrumble_phone)
    return text


# phone_numbers = extract_phone_numbers(text)
# print(phone_numbers)

# 대화 시작
print("모델과 대화를 시작합니다. 종료하려면 '종료'라고 입력하세요.")
messages = []
while True:
    user_content = input("사용자 : ")
    messages.append({"role": "user", "content": f"{user_content}->"})    

    if user_content == "종료":
        break
    
    # 사용자 입력을 모델에 전달하여 응답 받기
    # assistant_content = str(chat_with_model(user_content)).split('\n')[0]
    assistant_content = chat_with_model(user_content)

    answer = assistant_content.split('\n')[0]
    messages.append({"role": "assistant", "content": f"{answer}"})
    
    print(f"GPT : {extract_phone_numbers(answer)}")
    print('--------------------------------------------------------------')

