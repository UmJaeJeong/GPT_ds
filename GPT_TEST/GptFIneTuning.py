import openai
from utils.JsonParse import JsonParse

# OpenAI API 키 설정
openai.api_key = ""

#학습파일 업로드 
def upload_file(file_path):
    with open(file_path, "rb") as file:
        response = openai.File.create(
            file=file,
            purpose='fine-tune'
        )
        file_id = response['id']
        print(f"*** 학습파일업로드 ***\n{response}\n")

        return file_id

 #등록된 파일 파인튜닝   
def fine_tune_model(training_file):
    response = openai.FineTune.create(training_file=training_file)
    print(f"*** 등록된 파일 파인튜닝 ***\n{response}\n")
    return response

#파인튜닝된 목록
def fine_tune_model_list():
    response = openai.FineTune.list()
    print(f"*** 파인튜닝된 목록 ***")
    model_list = JsonParse.JsonOutputTunedList(response)
    fine_tuned_list_print(model_list)
    return model_list

#파인튜닝 삭제
def fine_tune_model_delete(fine_tuned_model):
    response = openai.Model.delete(fine_tuned_model)
    print(f"*** 파인튜닝 삭제 ***\n{response}\n")
    return

def fine_tune_cancel(model_name):
    openai.FineTune.cancel(id=model_name)
    return

def fine_tuned_list_print(model_list):
    if model_list is not None:
        for model in model_list:
            print(f"{model}")
    else:
        print('The list is None')

# # 파일 업로드 실행
# file_path = "example_prepared.jsonl"  # 업로드할 파일 경로
# file_id = upload_file(file_path)
# print(f"File uploaded successfully. File ID: {file_id}")

# # #업로된 파일 파인튜닝(학습)
# training_file = file_id  # 학습 파일의 ID 또는 경로
# response = fine_tune_model(training_file)

#파인튜닝 목록 실행 / 튜닝모델만 파싱해서 출력
# mode_list = fine_tune_model_list()


#파인튜닝 삭제 (1개)
# fine_tune_model_delete('')

#파인튜닝 리스트 전체 삭제 / 목록실행과 같이 사용 
# for fine_tuned_model in mode_list:
#     print(fine_tuned_model)
#     # fine_tune_model_delete(fine_tuned_model)
#     fine_tune_cancel(fine_tuned_model)


# 응답 값 활용 예시
# model_id = response['model']
# status = response['status']
# print(f"Fine-tuned model ID: {model_id}")
# print(f"Fine-tuning status: {status}")

#여기까지만해서 파인튜닝 생성하면 playground에서 model명이 추가된것이 확인된다. 
#모델명 ex) curie:ft-personal-2023-06-21-08-32-40
#모델명 ex) davinci:ft-personal-2023-06-21-08-32-40


# print("파인튜닝 목록")
response = openai.FineTune.list()
print(response)


#업로드 파일 리스트
# response = JsonParse.JsonOutputUploadFileList(openai.File.list())
# print(response)

#파일삭제
# for file in response:
#     res = openai.File.delete(file)
#     print(res)

