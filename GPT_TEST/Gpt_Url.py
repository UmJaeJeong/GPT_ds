import requests
from bs4 import BeautifulSoup
import openai

# OpenAI API 인증 설정
openai.api_key = "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"

def extract_text_from_website(url):
    # 웹사이트에 GET 요청을 보냅니다.
    response = requests.get(url)
    
    # 요청이 성공한 경우에만 추출 작업을 수행합니다.
    if response.status_code == 200:
        # HTML 문서를 파싱합니다.
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 모든 텍스트를 추출합니다.
        text = soup.get_text().replace('\n','')
        # for tag in program_names:
        #     print(tag.get_next())
        
        return text
    else:
        print("오류: 웹사이트에 접근할 수 없습니다.")
        return None

# 추출할 웹사이트의 링크
url = "https://cjhong.tistory.com/151"

# 텍스트 추출 함수 호출
extracted_text = extract_text_from_website(url)

if extracted_text:
    print(extracted_text)


    messages = [{"role": "assistant", "content": f"{extracted_text}"}]
print("모델과 대화를 시작합니다. 종료하려면 '종료'라고 입력하세요.")
while True:
    user_content = input("사용자 : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")


    #image -> Text
    #[Text from: ~~~~~]