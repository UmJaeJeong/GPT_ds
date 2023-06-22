import json

class JsonParse:
    
    #파인튜닝된 리스트만 출력(파인튜닝 모델명만 )
    @staticmethod
    def JsonOutputTunedList(response):
        response_data = json.loads(str(response))
        fine_tuned_models = []
        for data in response_data['data']:
            fine_tuned_models.append(data['fine_tuned_model'])
        # print(fine_tuned_models)   
        return fine_tuned_models
    
    