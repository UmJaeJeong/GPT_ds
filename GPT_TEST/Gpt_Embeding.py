# imports
import ast  # for converting embeddings saved as strings back to arrays
import openai  # for calling the OpenAI API
import pandas as pd  # for storing text and embeddings data

openai.api_key = "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"  # supply your API key however you choose


# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"


wikipedia_article_on_curling = """KTds에는 7개의 본부가 있다.

총 7개의 본부이며,  고객서비스본부, 경영서비스본부, 플랫폼서비스본부, AI/CX 서비스본부, 인프라서비스 본부, Enterprise 사업본부, DX사업본부가 있다.
고객서비스본부에는 총 4개의 담당이 있으며, CRM담당, 고객담당, 빌링담당이 있으며 고객서비스본부에 소속되어있다..
빌링담당에는 4개의 팀이 있으며, 빌링운영팀, 빌링개발팀, PAY서비스팀, Rater서비스팀은 빌링담당에 소속되어있다..
Rater팀은 고객서비스본부에 소속되어있다. """




# an example question about the 2022 Olympics
question = 'Rater 서비스팀은 무슨 본부야?'

response = openai.ChatCompletion.create(
    messages=[
        {'role': 'system', 'content': '너는 KTds의 구성을 알고 Rater 서비스팀에 대해서 대답한다.'},
        {'role': 'user', 'content': question},
    ],
    model=GPT_MODEL,
    temperature=0,
)

print(response['choices'][0]['message']['content'])