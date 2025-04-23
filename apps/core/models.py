from django.db import models
import uuid



class Task(models.Model):
    # 고유 식별자 (UUID 사용)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 사용자의 원본 입력 텍스트
    user_input = models.TextField(blank=True, null=True, verbose_name="사용자 입력")

    # 작업 제목 (AI가 생성하거나 사용자가 명시)
    title = models.CharField(max_length=255, verbose_name="작업 제목")

    # AI가 생성한 세부 계획 또는 내용
    details = models.TextField(blank=True, null=True, verbose_name="세부 계획/내용")

    # 작업 상태 (선택 목록 방식 고려 가능)
    status = models.CharField(max_length=50, default="To Do", verbose_name="상태")

    # 생성 및 수정 시각 자동 기록
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    # 연결된 Notion 페이지 ID
    notion_page_id = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name="Notion 페이지 ID")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = '작업'
        verbose_name_plural = '작업 목록'