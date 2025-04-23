from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskInputSerializer, TaskSerializer
from apps.core.models import Task
from apps.core.services.task_service import process_and_create_task
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
        if input_serializer.is_valid():
            user_input = input_serializer.validated_data['text']

            # 핵심 로직 처리 함수 호출
            created_task, error_msg = process_and_create_task(user_input)

            if created_task:
                output_serializer = TaskSerializer(created_task)
                return Response(output_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": error_msg or "알 수 없는 오류 발생"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    