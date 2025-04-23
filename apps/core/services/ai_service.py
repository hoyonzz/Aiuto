import google.generativeai as genai
from django.conf import settings
import json
import traceback
import re



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
        print(f"INFO: Using Google AI Model: {self.model.model_name}") # 사용 중인 모델 이름 확인용 로그 추가

    def generate_task_plan(self, user_input: str):
        # 사용자 입력을 바탕으로 작업 계획 생성
        category_options = "아이디어/메모, 가족/집안일, 학습/스터디, 건강/운동, 금융/재테크, 자기계발, 개인, 약속, 업무"
        priority_options = "긴급, 중요, 나중"

        prompt = f"""
        당신은 유능한 AI 비서입니다. 다음 사용자 요청을 분석하여, Notion 데이터베이스에 기록할 구조화된 작업 계획을 JSON 형식으로 생성해주세요.
        JSON 객체는 다음 키들을 포함해야 합니다:
        - "title": 생성될 작업의 제목 (Notion의 '테스크' 속성에 해당)
        - "details": 작업을 완료하기 위한 구체적인 단계별 계획 또는 필요한 정보 요약 (Notion 페이지 본문에 해당, Markdown 리스트 형식 선호)
        - "status": 작업의 초기 상태. 기본값은 "예정". (Notion의 '상태' Select 속성에 해당, 옵션: "예정", "후속조치", "연기", "완료")
        - "due_date": 작업의 예상 마감일 또는 관련 날짜 (YYYY-MM-DD 형식). 날짜를 특정할 수 없으면 null 또는 빈 문자열. (Notion의 '날짜' Date 속성에 해당)
        - "categories": 작업의 분류. 다음 옵션 중에서 가장 관련성이 높은 것들을 쉼표로 구분하여 제안해주세요: [{category_options}]. (Notion의 '카테고리' Multi-select 속성에 해당)
        - "priority": 작업의 중요도. 다음 옵션 중에서 가장 적절한 것 하나를 제안해주세요: [{priority_options}]. 관련 정보가 부족하면 null 또는 빈 문자열. (Notion의 '우선순위' Select 속성에 해당)


        결과는 다른 설명이나 주석 없이 순수한 JSON 형식으로만 반환해주세요.
        
        사용자 요청: "{user_input}"
        
        JSON 출력 예시:
        {{{{
        "title": "...",
        "details": "...",
        "status": "예정",
        "due_date": "2024-05-11",
        "categories": "업무, 자기계발",
        "priority": "중요"
        }}}}
        """

        try:
            print("DEBUG: Calling Google AI API...")
            response = self.model.generate_content(prompt)
            print(f"DEBUG: AI Raw Response Text:\n{response.text}")

            # 응답 텍스트 정리
            cleaned_response = response.text.strip()
            if cleaned_response.startswith("```json"):
                cleaned_response = cleaned_response[7:]
            if cleaned_response.endswith("```"):
                cleaned_response = cleaned_response[:-3]
            cleaned_response = cleaned_response.strip()

            cleaned_response = re.sub(r"/\*.*?\*/", "", cleaned_response, flags=re.DOTALL)

            print(f"DEBUG: Cleaned AI Response Text (after comment removal):\n{cleaned_response}")

            plan_data = json.loads(cleaned_response)
            print("DEBUG: Successfully parsed AI response JSON.")

            return plan_data
        
        except json.JSONDecodeError as e:
            print(f"ERROR: AI 응답 JSON 파싱 실패: {e}")
            print(f"AI 원본 응답 (오류 발생 시): {response.text}")
            print(f"파싱 시도한 텍스트: {cleaned_response}") # 파싱 실패 시 어떤 텍스트로 시도했는지 확인
            return { ... } # 이전과 동일한 대체 데이터
        except Exception as e:
            print(f"ERROR: Google AI 서비스 처리 중 예외 발생: {e}")
            traceback.print_exc()
            return { ... } # 이전과 동일한 대체 데이터
        

ai_service = AIService()
