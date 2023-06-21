import openai

# OpenAI API 키 설정
openai.api_key = "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"

def upload_file(file_path):
    with open(file_path, "rb") as file:
        response = openai.File.create(
            file=file,
            purpose='fine-tune'
        )
        file_id = response['id']
        print(f"결과1 : {response}")
        return file_id
    
def fine_tune_model(training_file):
    print("파인튜닝 create\n")
    response = openai.FineTune.create(training_file=training_file)
    return response


# 파일 업로드 예시
file_path = "example1_prepared.jsonl"  # 업로드할 파일 경로
file_id = upload_file(file_path)
print(f"File uploaded successfully. File ID: {file_id}")

training_file = file_id  # 학습 파일의 ID 또는 경로
response = fine_tune_model(training_file)
print(response)


# 응답 값 활용 예시
model_id = response['model']
status = response['status']
print(f"Fine-tuned model ID: {model_id}")
print(f"Fine-tuning status: {status}")

print("파인튜닝 생성 끝 ")

#여기까지만해서 파인튜닝 생성하면 playground에서 model명이 추가된것이 확인된다. 
#모델명 ex) curie:ft-personal-2023-06-21-08-32-40
#모델명 ex) davinci:ft-personal-2023-06-21-08-32-40



# print("파인튜닝 목록")

# response = openai.FineTune.list()
# print(response)
