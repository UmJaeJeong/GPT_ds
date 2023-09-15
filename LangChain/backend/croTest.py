
from bs4 import BeautifulSoup
# selenium 4.x 버전 사용시
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import openai


# OpenAI API 인증 설정
openai.api_key = "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"

#최대 문맥 길이
# MAX_CONTEXT_LENGTH = 4000
messages = []

# 크롬 드라이버 생성
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 크롬 드라이버 설치 및 업데이트
# chromedriver_autoinstaller.install()

#ChromeDriver와 
# 웹 드라이버 생성
path = 'C:/Users/umjae/Downloads/chromedriver_win32/chromedriver.exe'


driver = webdriver.Chrome(path)
google_url = f"https://product.kt.com/wDic/index.do?CateCode=6002"
    
# 구글 검색 페이지 열기
driver.get(google_url)
    
# 페이지 소스 가져오기
page_source = driver.page_source
    
# BeautifulSoup을 사용하여 페이지 소스 파싱
soup = BeautifulSoup(page_source, "html.parser")
    
# 모든 텍스트 추출
all_text = soup.get_text().replace(" ","").replace("\n","").replace("\t","")
print(all_text)



messages.append({"role": "assistant", "content": f"{all_text}"})
try:
    # completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages, max_tokens=MAX_CONTEXT_LENGTH)
    completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)

except Exception as e:
    # print(e)
    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Token Over@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    messages.pop(0)



print("모델과 대화를 시작합니다. 종료하려면 '종료'라고 입력하세요.")
while True:
    user_content = input("사용자 : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    try:
        completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)
    except Exception as e:
        print(e)
        messages.pop(0)
        total_messages = len(messages)
        print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Token Over@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

        # print("messages 리스트의 총 길이:", total_messages)
        # for msg in messages:
        #     print(msg)
        continue
        

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")



# 웹 드라이버 종료
# driver.quit()
