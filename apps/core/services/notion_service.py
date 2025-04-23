import os
from notion_client import Client
from django.conf import settings
from notion_client.errors import APIResponseError # Notion API 오류 처리용


class NotionService:
    def __init__(self):
        api_key = settings.NOTION_API_KEY
        db_id = settings.NOTION_DATABASE_ID

        # 값이 없는 경우 오류 발생시키기
        if not api_key:
            raise ValueError("Notion API Key is not in settings.")
                
        if not db_id:
            raise ValueError("Notion Database ID is not in settings.")
        
        self.client = Client(auth=api_key)
        self.database_id = db_id
        # 초기화 완료

        print("NotionService initialized successfully.")
        # 초기화 성공 메세지

    def add_task(self, title: str, details: str = "", properties: dict = None):
        # Notion 데이터베이스에 새 페이지를 추가
        
        
        # 서비스가 제대로 초기화되지 않았을 경우 방어 코드
        if not hasattr(self, 'client') or not hasattr(self, 'database_id'):
            print("ERROR: NotionService is not properly initialized.")
            return None
        
        if properties is None:
            properties = {}

        page_properties = {
            "title": {
                "title": [{"text": {"content": title}}]
            }
        }

        page_properties.update(properties)

        children = []
        if details:
            children.append({
                'object': 'block',
                'type': 'paragraph',
                'paragraph': {
                    "rich_text": [{"type": "text", "text": {"content": details}}]
                }
            })

        try:
            response = self.client.pages.create(
                parent={"database_id": self.database_id},
                properties=page_properties,
                children=children
            )
            print(f"Successfully created Notion page: {response.get('id')}")
            return response
        
        # Notion API 오류를 좀 더 구체적으로 처리
        except APIResponseError as e:
            print(f"Notion API Error creating page: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error creating Notion page: {e}")
            return None
        
# 싱글톤처럼 사용하기 위해 인스턴스 생성 (선택 사항)
notion_service = NotionService()