from rest_framework import serializers
from apps.core.models import Task



class TaskSerializer(serializers.ModelSerializer):
    # Task 모델 테이터를 JSON으로 변환
    class Meta:
        model = Task
        # API를 통해 보여줄 필드 목록
        fields = [
            'id',
            'user_input',
            'title',
            'details',
            'status',
            'notion_page_id',
            'created_at',
            'updated_at',
        ]

        # 읽기 전용 필드 설정
        read_only_fields = ['id', 'created_at', 'updated_at']

class TaskInputSerializer(serializers.Serializer):
    # 사용자로부터 API 요청을 통해 입력을 받기 위한 Serializer
    # 사용자가 안드로이드 등에서 보낼 텍스트 데이터
    text = serializers.CharField(max_length=1000, required=True, help_text="사용자가 입력한 할 일, 아이디어 등의 텍스트 내용")
    
    # 필요에 따라 다른 입력 필드 추가 기능(예: 특정 날짜 지정 등)
    # due_date = serializers.DateField(required=False, help_text="작업 마감일(선택)")