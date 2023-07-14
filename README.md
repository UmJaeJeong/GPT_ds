# GPT_ds
GPT, 파인튜닝


아래의 에러코드 참고
openai.error.ratelimiterror: you exceeded your current quota, please check your plan and billing details.
=> 현재 무료량을 초과했다는 의미인데... 결제수단을 등록하면 해결가능하다고 되어 있으나,
   결제수단 등록시 바로 구독되기 떄문에 다른 방안을 찾아봐야함
--------------------------------------------------------------------------
GptFineTuning.py
로직 플로우
1) .jsonl파일 업로드(프롬프트에 맞춰야할)
2) fintuning 생성
3) playground에서 생성된 모델을 확인가능




--------------------------------------------------------------------------
CLI 
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
(프롬프트 만들기) 



J5yGGbDiaSH8jClT5pxdT3BlbkFJZyEGorEOAK9IWmyAMtHu

