import openai
import re

#환경설정에 등록된 key값 
# openai.api_key = os.getenv("OPENAI_API_KEY")

#Chat-GPT4로 했을때 채팅이 가능하고 / GPT3는 채팅이 불가능핟 그래서 히스토리를 사용행야함

# OpenAI API 인증 설정
openai.api_key = "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"

input_text = """
아래 내용은 정리되지 않은 html형태의 데이터 입니다. 당신은 아래 내용을 평문으로작성해야만 합니다.
<p class="pduct-tbl-top-desc">부가세가 포함된 실제 지불금액입니다.</p>
<table class="pduct-tbl-plan" style="table-layout: inherit;">
<caption class="invisible">요금제, 월정액, 데이터, 데이터 로밍, 음성, 문자, 제공혜택(멤버십, 단말보험, 스마트기기,Y덤), 프로모션 혜택(24개월간 제공) 으로 정의한 표</caption>
<colgroup>
<col style="width: 8%;"/>
<col style="width: 8%;"/>
<col style="width: 6%;"/>
<col style="width: 8%;"/>
<col style="width: 9%;"/>
<col style="width: 5%;"/>
<col style="width: 6%;"/>
<col style="width: 12%;"/>
<col style="width: 10%;"/>
<col style="width: 8%;"/>
<col style="width: 13%;"/>
</colgroup>
<thead>
<tr>
<th rowspan="2" scope="col">요금제</th>
<th rowspan="2" scope="col">월정액</th>
<th rowspan="2" scope="col">데이터</th>
<th rowspan="2" scope="col">데이터<br/>
                        로밍</th>
<th rowspan="2" scope="col">음성</th>
<th rowspan="2" scope="col">문자</th>
<th colspan="4" scope="colgroup">제공혜택</th>
<th colspan="2" rowspan="2" scope="col">프로모션 혜택<br/>
                        (24개월간 제공)</th>
</tr>
<tr class="row">
<th scope="col">멤버십</th>
<th scope="col">단말보험</th>
<th scope="col">스마트기기<br/>
                        또는<br/>
                        데이터 쉐어링</th>
<th scope="col">Y덤*<br/>
                        (만 29세이하)</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row">스페셜</th>
<td>100,000원</td>
<td rowspan="2">완전<br/>
                        무제한</td>
<td rowspan="2">무제한<br/>
                        (최대 100Kbps<br/>
                        속도제어)</td>
<td rowspan="2">집/이동전화<br/>
                        무제한<br/>
                        (+영상/부가 300분)</td>
<td rowspan="2">기본<br/>
                        제공</td>
<td>VVIP<br/>
                        제공</td>
<td>단말보험<br/>
                        월정액 멤버십<br/>
                        차감<br/>
                        월 최대 4,500P<br/>
                        (애플케어팩<br/>
                        제외, 플러스<br/>
                        서비스료 제외)</td>
<td>1회선 무료<br/>
<a class="btn small is-line-lightgray" href="https://direct.kt.com/direct/directShare.do" target="_blank" title="새창열림">셀프 개통하기</a></td>
<td class="td-left" rowspan="2">
<ul class="pduct-list">
<li>공유데이터 2배 제공</li>
<li>(베이직) 스마트기기 1회선 50% 할인</li>
</ul>
</td>
<td class="td-left" rowspan="2">[50% 할인 혜택]
                        <ul class="pduct-list">
<li>디즈니+ (‘23년말까지 무료**)</li>
<li>티빙</li>
<li>지니뮤직</li>
<li>밀리의 서재</li>
<li>블라이스</li>
</ul>
</td>
<td rowspan="2">택1</td>
</tr>
<tr>
<th scope="row">베이직</th>
<td>80,000원</td>
<td>VIP<br/>
                        제공</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>
<ul btn="" class="pduct-list">
<li>(*) Y덤 혜택은 만 29세 이하 고객 대상으로 제공됩니다. 자세한 사항은 아래 <y덤> 내용을 참고해주세요.</y덤></li>
<li>(**) 디즈니+ 혜택 선택 시, '23.12.31까지 무료로 제공하며 '24.1.1부터 50% 할인 혜택을 적용 합니다.</li>
<li>멤버십 VVIP 혜택 <a class="btn small is-line-lightgray" href="http://membership.kt.com/vip/choice/VvipChoiceInfo.do" target="_blank" title="새창열림">자세히 보기</a>, 멤버십 VIP 혜택 
<a class="btn small is-line-lightgray" href="http://membership.kt.com/vip/choice/ChoiceInfo.do" target="_blank" title="새창열림">자세히 보기</a></li>
<li>만29세이하 Y덤 혜택 <a class="btn small is-line-lightgray" href="https://product.kt.com/benefit/membership/web/y-bonus.html" target="_blank" title="새창열림">자세히 보기</a>, 티빙 OTT구독 할인 <a class="btn small is-line-lightgray" href="https://product.kt.com/wDic/simple/ottMain.do" target="_blank" title="새창열림">자세히 보기</a>, Google One 100GB 제공 <a class="btn small is-line-lightgray y-bonus-qr_button" href="#ybonusQRLayer">자세히 보기</a></li>
</ul>
<div class="y-bonus-qr" id="ybonusQRLayer">
<div class="y-bonus-qr_aligner">
<div class="y-bonus-qr_box">
<div class="y-bonus-qr_image"><img alt="QR코드 이미지" src="/static/prodetail/common/images/QRpopup/y-bonus-qr_image.png"/></div>
<a class="y-bonus-qr_close" href="javascript:'';">팝업 닫기</a></div>
</div>
</div>
<script type="text/javascript">
        $j('.y-bonus-qr_button').each(function(){
                var ybonusTrigger = $j(this),
                         ybonusQRlayer = ybonusTrigger.attr('href');

                ybonusTrigger.on('click', function(){
                        $j(ybonusQRlayer).addClass('active').focus();
                        return false;
                });

                $j('.y-bonus-qr_close').on('click', function(){
                        $j(ybonusQRlayer).removeClass('active');
                        ybonusTrigger.focus();
                        return false;
                });
        });
</script><strong class="pduct-tit">&lt; 우리 아이 할인 혜택 &gt;</strong>
<ul class="pduct-desh-list">
<li>대상: 초이스 프리미엄 , 초이스 스페셜 이용 고객</li>
<li>혜택: 주니어 요금제 (5G 주니어, 5G 주니어 슬림, LTE 주니어 슬림) 월 8,800원 할인</li>
<li>제공기간: 초이스 프리미엄 , 초이스 스페셜 이용 기간 동안 지속 제공
        <ul class="pduct-noted-list">
<li>스마트기기 1회선 무료혜택과 중복 적용되지 않으며, 기타 자세한 사항은 ‘가입 및 유의사항‘ 참고</li>
</ul>
</li>
</ul>

1. 위 내용을 전부 읽기 쉽도록 평문으로 재작성해 주세요. 이 요구조건은 매우 중요하며 꼭 지켜져야합니다. 임의로 정리하거나 소제목을 붙이지 마세요. 끊어서 작성하지 말고 반드시 하나의 평문이어야합니다.
"""

# 이 코드를 실행하면 input_text 변수에 주어진 내용이 저장됩니다.


messages = []
# while True:
#     # user_content = input("사용자 : ")
#     messages.append({"role": "user", "content": f"{input_text}"})

#     completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)

#     assistant_content = completion.choices[0].message["content"].strip()

#     messages.append({"role": "assistant", "content": f"{assistant_content}"})

#     print(f"GPT : {assistant_content}")

messages.append({"role": "user", "content": f"{input_text}"})

completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages)

assistant_content = completion.choices[0].message["content"].strip()

messages.append({"role": "assistant", "content": f"{assistant_content}"})

print(f"GPT : {assistant_content}")
