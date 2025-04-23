from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskInputSerializer, TaskSerializer
from apps.core.models import Task
from apps.core.services.notion_service import notion_service
from apps.core.services.ai_service import ai_service
# from rest_framework.permissions import BasePermission
from django.conf import settings
import datetime



# # 간단한 API 키 인증 예시
# class SimpleAPIKeyPermission(BasePermission):
#     def has_permission(self, request, view):
#         # 실제로는 settings 등에서 키를 가져와 비교
#         api_key = request.headers.get('X-API-KEY')
#         return api_key == 'YOUR_SECRET_API_KEY_HERE' # 실제 키로 대체하고 안전하게 관리

class TaskCreateAPIView(APIView):
    # 사용자 입력을 받아 AI 처리 후 Notion에 기록하고 DB에 저장하는 API
    # permission_classes = [SimpleAPIKeyPermission] # (선택) API 키 인증 적용

    def post(self, request, *args, **kwargs):
        # 1. 사용자 입력 받기 및 유효성 검증
        input_serializer = TaskInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_text = input_serializer.validated_data['text']
        print(f"INFO: Received task input: {user_text}")

        # 2. AI 서비스 호출하여 계획 생성
        try:
            ai_plan = ai_service.generate_task_plan(user_text)
            # AI응답 유효성 검사 강화
            if not isinstance(ai_plan, dict) or 'title' not in ai_plan:
                print(f"ERROR: Invalid AI plan structure received: {ai_plan}")
                # 오류 처리 방식 결정 (여기서는 기본값으로 진행)
                ai_plan = {
                    "title": f"{user_text} (AI 구조 오류)",
                    "details": f"AI로부터 유효한 계획 구조를 받지 못했습니다. 응답: {ai_plan}",
                    "status": "예정", # 기본값
                }
        except Exception as e:
            print(f"ERROR: AI Service call failed: {e}")
            # 오류 처리 방식 결정
            ai_plan = {
                "title": f"{user_text} (AI 호출 오류)",
                "details": f"AI 서비스 호출 중 예외 발생: {e}",
                "status": "예정",
            }

        # Notion 속성 구성 준비
        notion_properties = {}

        TITLE_PROPERTY_NAME = "title"
        STATUS_PROPERTY_NAME = "상태"
        DATE_PROPERTY_NAME = "날짜"
        CATEGORY_PROPERTY_NAME = "카테고리"
        PRIORITY_PROPERTY_NAME = "중요도"
        INPUT_DONE_PROPERTY_NAME = "입력완료"
        # AI 응답에서 값 추출 (없을 경우 대비 기본값 또는 None 사용)
        ai_title = ai_plan.get('title', f"{user_text} (제목 없음)")
        ai_details = ai_plan.get('details', '')
        ai_status = ai_plan.get('status', '예정') # 기본값 '예정'
        ai_due_date = ai_plan.get('due_date') # YYYY-MM-DD 형식 기대
        ai_categories_str = ai_plan.get('categories') # 쉼표 구분 문자열 기대
        ai_priority = ai_plan.get('priority') # '긴급', '중요', '나중' 기대

        # Notion 속성 매핑
        # 1. 상태(Select 타입) -키를 상태로, 값 타입을 status로
        valid_statuses = ["예정", "후속조치", "연기", "완료"]
        if ai_status in valid_statuses:
            notion_properties[STATUS_PROPERTY_NAME] = {"status" : {"name": ai_status}}
            print(f"DEBUG: Setting Notion '{STATUS_PROPERTY_NAME}' to: {ai_status}")
        else:
            notion_properties[STATUS_PROPERTY_NAME] = {"status" : {"name":"예정"}} # 유효하지 않으면 기본값
            print(f"WARNING: Invalid status '{ai_status}', defaulting to '예정'.")

        # 2. 날짜 (Date 타입) - Notion 속성 이름: '날짜'
        if ai_due_date and isinstance(ai_due_date, str):
            # 간단한 YYYY-MM0DD 형식 체크
            if len(ai_due_date) == 10 and ai_due_date[4] == '-' and ai_due_date[7] == '-':
                notion_properties[DATE_PROPERTY_NAME] = {"date": {"start": ai_due_date}}
                print(f"DEBUG: Setting Notion '{DATE_PROPERTY_NAME}' to: {ai_due_date}")
            else:
                print(f"WARNING: Invalid date format for '{DATE_PROPERTY_NAME}': {ai_due_date}. Date not set.")
                ai_due_date = None # 이후 DB 저장을 위해 None 처리
        
        # 3. 카테고리 (Multi-select 타입) - Notion 속성 이름: 카테고리
        if ai_categories_str and isinstance(ai_categories_str, str):
            valid_category_options = ["아이디어/메모", "가족/집안일", "학습/스터디", "건강/운동", "금융/재태크", "자기계발", "개인", "약속", "업무"]
            categories_list = []
            for cat in ai_categories_str.split(','):
                clean_cat = cat.strip()
                if clean_cat and clean_cat in valid_category_options:
                    categories_list.append({"name": clean_cat})
                else:
                    print(f"WARNING: Invalid or unknown category '{clean_cat}' suggested by AI.")
            if categories_list:
                notion_properties[CATEGORY_PROPERTY_NAME] = {"multi_select": categories_list}
                print(f"DEBUG: Setting Notion '{CATEGORY_PROPERTY_NAME}' to: {categories_list}")
        
        # 4. 우선순위 (Select 타입) - Notion 속성 이름: '우선순위'
        valid_priorities = ["긴급", "중요", "나중"]
        if ai_priority and ai_priority in valid_priorities:
            notion_properties[PRIORITY_PROPERTY_NAME] = {"select": {"name": ai_priority}}
            print(f"DEBUG: Setting Notion '{PRIORITY_PROPERTY_NAME}' to: {ai_priority}")
        else:
            # 우선순위가 없거나 유효하지 않으면 설정하지 않음 또는 기본값 나중으로 설정 가능
            print(f"WARNING: Invalid or missing priority '{ai_priority}'. Priority not set.")
            ai_priority = None

        # 5. 입력완료 (Checkbox타입) - Notion 속성 이름: 입력완료
        notion_properties[INPUT_DONE_PROPERTY_NAME] = {"checkbox": True}
        print(f"DEBUG: Setting Notion '{INPUT_DONE_PROPERTY_NAME}' to: True")



        
        # 3. Notion 서비스 호출하여 페이지 생성
        try:
            # notion_properties = {} #Notion 속성 준비
            # AI가 제안한 속성이 있다면 여기에 추가하는 로직 (선택 사항)
            # 예: if 'suggested_properties' in ai_plan and '상태' in ai_plan['suggested_properties']:
            #         notion_properties['상태'] = {"select": {"name": ai_plan['suggested_properties']['상태']}}

            notion_response = notion_service.add_task(
                title=ai_title,
                details=ai_details,
                properties=notion_properties,
            )
            notion_page_id = notion_response.get('id') if notion_response else None
            if notion_page_id:
                print(f"INFO: Successfully created Notion page: {notion_page_id}")
            else:
                print("WARNING: Failed to create Notion page. Proceeding without Notion ID.")
                # Notion 생성 실패 시 어떻게 처리할지 정책 필요 (예: 로깅, 상태 변경 등)
        
        except Exception as e:
            print(f"ERROR: Notion Service call failed: {e}")
            # Notion 호출 실패해도 DB 저장은 시도하도록 할 수 있음(선택)
            notion_page_id = None
            # return Response({"error": "Notion 연동 중 예외가 발생했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # 4. Task 모델 인스턴스 생성 및 DB 저장
        try:
            task = Task.objects.create(
                user_input=user_text,
                title=ai_plan.get('title', '제목 없음'),
                details=ai_plan.get('details', ''),
                status=ai_plan.get('status', 'To Do'), # AI 응답 또는 기본값 사용
                notion_page_id=notion_page_id
            )
            print(f"INFO: Successfully saved Task to DB: {task.id}")
        except Exception as e:
            print(f"ERROR: Failed to save Task to DB: {e}")
            return Response({"error": "작업을 데이터베이스에 저장하는 중 오류가 발생했습니다."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # 5. 생성된 Task 정보 응답 (JSON)
        output_serializer = TaskSerializer(task)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
    
    