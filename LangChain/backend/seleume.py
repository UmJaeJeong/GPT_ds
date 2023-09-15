from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import openai
import time
from selenium.webdriver.common.by import By
import datetime


# OpenAI API 인증 설정
openai.api_key = "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"

# 크롬 드라이버 생성
path = 'C:/Users/umjae/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
#5G심플
# google_url = f"https://product.kt.com/wDic/productDetail.do?ItemCode=1406&CateCode=6002&filter_code=81&option_code=109&pageSize=10"
#5G Y슬림
# google_url = f"https://product.kt.com/wDic/productDetail.do?ItemCode=1359&CateCode=6002&filter_code=81&option_code=109&pageSize=10"
#5G슬림
# google_url = f"https://product.kt.com/wDic/productDetail.do?ItemCode=1284&CateCode=6002&filter_code=81&option_code=109&pageSize=10"
#5G주니어
google_url = f"https://product.kt.com/wDic/productDetail.do?ItemCode=1480&CateCode=6002&filter_code=81&option_code=109&pageSize=10"

# 특정 페이지 열기
driver.get(google_url)

# HTMl 소스에서 주석 제거한 클린소스
def cleanHtmlSource(driver):
    try:
        # class가 ''인 div 태그 찾기
        div_element = driver.find_element_by_id('appendPriceDiv')

        # div 태그 내부의 HTML 코드 가져오기
        inner_html = div_element.get_attribute('innerHTML')

        # HTML 파싱
        soup = BeautifulSoup(inner_html, 'html.parser')

        # 주석 제거 기능
        for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
            comment.extract()

        # 주석이 제거된 HTML 코드 출력
        cleaned_html = str(soup)
        print(cleaned_html)

    except Exception as e:
        print("오류 발생:", e)

def clickAllBtn(driver):
    for i in range(4,0,-1):
        element_id =f'title{i}'
        if i==1:
            element = driver.find_element(By.XPATH,f"//div[@id='appendPriceDiv']")
            driver.execute_script("arguments[0].scrollIntoView();", element)
        element = driver.find_element(By.XPATH,f"//button[@id='{element_id}']").click()


        driver.implicitly_wait(10)
        time.sleep(1)
    
    extractHtml(driver)
    driver.quit()

def afterEventHtmlAllSource(driver):
    # 클래스가 "accordions active"인 div 태그 찾기
    accordions_active_div = driver.find_element_by_css_selector('div.accordions.active')

    # div 태그의 모든 하위 button 태그 찾기
    buttons = accordions_active_div.find_elements_by_tag_name('button')

    # 모든 button을 클릭
    for button in buttons:
        print("*******************************")
        button.click()
        driver.implicitly_wait(5)
        time.sleep(1)

    # 바로 하위의 div 태그를 XPath로 클릭
    # sub_div_list= accordions_active_div.find_element_by_xpath('./div')  # 바로 하위 div 태그를 선택
    # sub_div_list = accordions_active_div.find_elements_by_xpath('./div')  # 바로 하위 div 태그를 모두 선택

    # div 태그 클릭
    # for  sub_div in sub_div_list:
    #     print('12312321321321111')
    #     sub_div.click()
    #     driver.implicitly_wait(5)
        
def extractHtml(driver):
    # Html 전체 소스
    html_source = driver.page_source
    print(html_source)

    # 텍스트 파일로 저장
    saveTextFile(html_source)

def saveTextFile(text):
    # HTML 소스코드 저장
    with open("./backend/ktdata/"+getTime()+".txt", 'w', encoding='utf-8') as file:
        file.write(text)

def getTime():
    # 현재 날짜와 시간을 가져옵니다.
    current_time = datetime.datetime.now()

    # 원하는 형식으로 포맷팅합니다.
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    return formatted_time

# cleanHtmlSource(driver)
clickAllBtn(driver)
# afterEventHtmlAllSource(driver)
