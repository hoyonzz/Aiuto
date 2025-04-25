import google.generativeai as genai
from django.conf import settings
import json
import traceback
import re
from datetime import datetime, timedelta, timezone



class AIService:
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)

        # # 사용 가능 모델 출력 디버깅 코드
        # print("--- Available Generative Models ---")
        # for m in genai.list_models():
        #     if 'generateContent' in m.supported_generation_methods:
        #         print(f"Model Name: {m.name}")
        # print("-----------------------------------------")
        
        self.model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

    def generate_task_plan(self, user_input: str):
        # 사용자 입력을 바탕으로 작업 계획 생성
        category_options = "아이디어/메모, 가족/집안일, 학습/스터디, 건강/운동, 금융/재테크, 자기계발, 개인, 약속, 업무"
        priority_options = "긴급, 중요, 나중"

        kst = timezone(timedelta(hours=9))
        now_kst = datetime.now(kst)
        today_str = now_kst.strftime('%Y-%m-%d')


        prompt = f"""
        당신은 유능한 AI 비서입니다. 다음 사용자 요청을 분석하여, Notion 데이터베이스에 기록할 구조화된 작업 계획을 JSON 형식으로 생성해주세요.
        현재 날짜는 {today_str} (한국 시간 기준) 입니다. 모든 날짜 계산은 이 날짜를 기준으로 해주세요.

        JSON 객체는 다음 키들을 포함해야 합니다:
        - "title": 생성될 작업의 제목 (Notion의 '테스크' 속성에 해당)

        - "details": 작업을 완료하기 위한 구체적인 단계별 계획 또는 필요한 정보 요약 (Notion 페이지 본문에 해당, Markdown 리스트 형식 선호).
        작업 실행에 필요한 사전 확인 사항이나 외부 요인(예: 날씨 확인, 예약 필요 여부, 준비물 등)이 있다면 해당 내용도 단계에 포함시켜 주세요.
        (예를 들어, '세차하기'요청 시 '날씨 확인하기', '주변 세차장 정보', '준비물', '세차 팁 추천내용' 포함)
        
        - "status": 작업의 초기 상태. 기본값은 "예정". (Notion의 '상태' Select 속성에 해당, 옵션: "예정", "후속조치", "연기", "완료")
        
        - "due_date": 작업의 예상 마감일 또는 관련 날짜/시간. 
            - 사용자 입력에 '오늘'이 명시되면, 반드시 {today_str} 날짜를 사용하고 시간 정보가 있으면 아래 ISO 8601 형식으로 결합해주세요.
            - 날짜와 시간이 모두 명확하면 반드시 ISO 8601 형식 (YYYY-MM-DDTHH:mm:ss+09:00)으로 반환해주세요. (예: '{today_str} 기준 내일 아침 9시' ->
            '{(now_kst.date() + timedelta(days=1)).strftime('%Y-%m-%d') }T09:00:00+09:00
            - 날짜만 명확하거나, 사용자가 "다음 주", "내일" 등 상대적 날짜를 언급하면, 오늘 ({today_str})을 기준으로 계산하여 'YYYY-MM-DD' 형식으로만 반환해주세요.
            (예: '다음 주 월요일' -> 계산된 YYYY-MM-DD 값)
            - 날짜/시간을 특정할 수 없으면 반드시 null을 반환해주세요. (빈 문자열 아님)
                    
        - "categories": 작업의 분류. 다음 옵션 중에서 가장 알맞은 것만 쉼표로 구분하여 제안해주세요: [{category_options}]. (Notion의 '카테고리' Multi-select 속성에 해당)
        
        - "priority": 작업의 중요도. 다음 옵션 중에서 가장 적절한 것 하나를 제안해주세요: [{priority_options}].
        긴급 : 즉시 또는 오늘 내 처리 필요.
        중요 : 명확한 마감일이 있거나, 목표 달성에 필수적인 작업.
        나중 : 비교적 여유가 있거나, 일상적인 허드렛일
        요청내용만으로 중요도 판단이 어려우면 null 또는 문자열을 반환해주세요.(예를들어 '쓰레기 분리수거하기'는 '나중' 또는 null)



        결과는 다른 설명이나 주석 없이 순수한 JSON 형식으로만 반환해주세요.
        
        사용자 요청: "{user_input}"
        
        JSON 출력 예시:
        {{{{
        "title": "...",
        "details": "...",
        "status": "예정",
        "due_date": "{ (now_kst.date() + timedelta(days=1)).strftime('%Y-%m-%d') }T14:30:00+09:00", # 내일 오후 2시 30분 예시
        "categories": "업무, 자기계발",
        "priority": "중요"
        }}}}
        """

        try:
            print(f"DEBUG: Calling Google AI API with today's date: {today_str}")

            response = self.model.generate_content(prompt)
            # print(f"DEBUG: AI Raw Response Text:\n{response.text}")

            # 응답 텍스트 정리
            cleaned_response = response.text.strip()

            # 마크다운 코드 블록 제거
            if cleaned_response.startswith("```json"):
                cleaned_response = cleaned_response[7:]
            if cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[:-3]
            cleaned_response = cleaned_response.strip()

            cleaned_response = re.sub(r"/\*.*?\*/", "", cleaned_response, flags=re.DOTALL)

            # print(f"DEBUG: Cleaned AI Response Text (after comment removal):\n{cleaned_response}")

            plan_data = json.loads(cleaned_response)
            print("INFO: Successfully parsed AI response JSON.")
            
            return plan_data
        
        except json.JSONDecodeError as e:
            print(f"ERROR: AI 응답 JSON 파싱 실패: {e}")
            # print(f"AI 원본 응답 (오류 발생 시): {response.text}")
            print(f"파싱 시도한 텍스트: {cleaned_response}") # 파싱 실패 시 어떤 텍스트로 시도했는지 확인
            return {
                "title": f"{user_input} (AI 파싱 오류)",
                "details": f"AI 응답을 파싱하는 중 오류 발생: {e}. 원본 응답: {response.text[:500]}...",
                "status": "예정",
                "due_date": None,
                "categories": None,
                "priority": None,
             }
        
        except Exception as e:
            print(f"ERROR: Google AI 서비스 처리 중 예외 발생: {e}")
            traceback.print_exc()
            return {
                "title": f"{user_input} (AI 처리 오류)",
                "details": f"AI 응답을 파싱하는 중 오류 발생: {e}. 원본 응답: {response.text[:500]}...",
                "status": "예정",
                "due_date": None,
                "categories": None,
                "priority": None,
             }
        

ai_service = AIService()
