Backend 폴더
1. langchaind.py는 langchain을 이용하여 ktdata폴더에 있는 문서를 임베딩후 유사도 높은 문서를 k개 추출 후  추출한 문서에서 질문내용 검색
2. seleume.py는 주석으로 처리되어있는 변수(google_url)에 있는 요금제 내용을 Html 소스로 변환 후 ktdata폴더에 txt파일로 저장함 (파일명은 현재날짜시간)
3. main.py는 백엔드부분 소스코드 작업중(실행안됨)

1,2번을 각각 실행시켜 동작함 
이미ktdata 폴더에 요금제내용이 포함된 txt파일이 있음.




pip install openai
pip install langchain
pip install tiktoken
pip install chromadb

