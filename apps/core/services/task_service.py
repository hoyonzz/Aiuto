from .notion_service import notion_service
from .ai_service import ai_service
from ..models import Task



def process_and_create_task(user_input: str) -> tuple[Task | None, str | None]:
    # 사용자 입력을 받아 AI 처리, Notion 생성, DB 저장을 수행하고, 결과 Task 객체와 오류 메시지 반환
    print(f"INFO: Starting task processing for input: {user_input}")
    ai_plan = {}
    notion_page_id = None
    error_message = None
    task = None

    # 1. AI 서비스 호출
    try:
        ai_plan = ai_service.generate_task_plan(user_input)
        if not isinstance(ai_plan, dict) or 'title' not in ai_plan:
            print(f"ERROR: Invalid AI plan structure: {ai_plan}")
            error_message = "AI로부터 계획 구조를 받지 못했습니다."
            ai_plan = {"title": f"{user_input} (AI 구조 오류)", "details": error_message, "status":"예정"}
        else:
            print("DEBUG: Successfully parsed AI response JSON.")
    
    except Exception as e:
        print(f"ERROR: AI Service call failed: {e}")
        error_message = f"AI 서비스 호출 중 예외 발생: {e}"
        ai_plan = {"title": f"{user_input} (AI 호출 오류)", "details": error_message, "status": "예정"}

    # 2. Notion 속성 준비 및 페이지 생성
    try:
        notion_properties = {}
        STATUS_PROPERTY_NAME = "상태"
        DATE_PROPERTY_NAME = "날짜"
        CATEGORY_PROPERTY_NAME = "카테고리"
        PRIORITY_PROPERTY_NAME = "중요도"
        INPUT_DONE_PROPERTY_NAME = "입력완료"

        ai_status = ai_plan.get('status', '예정') # 기본값 '예정'
        ai_due_date = ai_plan.get('due_date') # YYYY-MM-DD 형식 기대
        ai_categories_str = ai_plan.get('categories') # 쉼표 구분 문자열 기대
        ai_priority = ai_plan.get('priority') # '긴급', '중요', '나중' 기대

        valid_statuses = ["예정", "후속조치", "연기", "완료"]
        if ai_status in valid_statuses:
            notion_properties[STATUS_PROPERTY_NAME] = {"status" : {"name": ai_status}}
        else:
            notion_properties[STATUS_PROPERTY_NAME] = {"status" : {"name":"예정"}} # 유효하지 않으면 기본값

        if ai_due_date and isinstance(ai_due_date, str) and len(ai_due_date) == 10:
            notion_properties[DATE_PROPERTY_NAME] = {"date": {"start": ai_due_date}}
        
        if ai_categories_str and isinstance(ai_categories_str, str):
            valid_category_options = ["아이디어/메모", "가족/집안일", "학습/스터디", "건강/운동", "금융/재태크", "자기계발", "개인", "약속", "업무"]
            categories_list = [{"name": cat.strip()} for cat in ai_categories_str.split(',') if cat.strip() in valid_category_options]
            if categories_list:
                notion_properties[CATEGORY_PROPERTY_NAME] = {"multi_select": categories_list}
        
        if PRIORITY_PROPERTY_NAME:
            valid_priorities = ["긴급", "중요", "나중"]
            if ai_priority and ai_priority in valid_priorities:
                notion_properties[PRIORITY_PROPERTY_NAME] = {"select": {"name": ai_priority}}

        if INPUT_DONE_PROPERTY_NAME:
            notion_properties[INPUT_DONE_PROPERTY_NAME] = {"checkbox": True}


        notion_response = notion_service.add_task(
            title=ai_plan.get('title', '제목 없음'),
            details=ai_plan.get('details', ''),
            properties=notion_properties
        )
        notion_page_id = notion_response.get('id') if notion_response else None
        if notion_page_id:
            print(f"INFO: Successfully created Notion page: {notion_page_id}")
        else:
            print("WARNING: Failed to create Notion page.")
            # Notion 실패해도 DB 저장은 진행
            # error_message = "Notion 페이지 생성에 실패했습니다." # 필요시 여러 메시지 설정

    except Exception as e:
        print(f"ERROR: Notion Service call failed: {e}")
        error_message = f'Notion 연동 중 예외가 발생했습니다: {e}'
        notion_page_id = None

    
    # 3. DB 저장
    try:
        task = Task.objects.create(
            user_input = user_input,
            title=ai_plan.get('title', '제목 없음'),
            details=ai_plan.get('details', ''),
            status=ai_plan.get('status', '예정'),
            notion_page_id=notion_page_id
        )
        print(f"INFO: Successfully saved Task to DB: {task.id}")
        return task, None

    except Exception as e:
        print(f"ERROR: Failed to save Task to DB: {e}")
        error_message = f'작업을 데이터베이스에 저장하는 중 오류 발생: {e}'
        return None, error_message