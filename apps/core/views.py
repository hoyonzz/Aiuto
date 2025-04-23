from django.shortcuts import render, redirect
from .services.task_service import process_and_create_task



def task_input_view(request):
    context = {}
    if request.method == 'POST':
        user_input = request.POST.get('user_text_input', '').strip()
        if user_input:
            created_task, error_msg = process_and_create_task(user_input)

            if created_task:
                context['message'] = f"'{created_task.title}' 작업이 성공적으로 등록되었습니다. (Notion ID: {created_task.notion_page_id})."
                # 성공 시 동일 페이지에 메시지 표시 또는 다른 페이지로 리다이렉트 가능
                # return redirect('some_success_rul')
            else:
                context['error'] = f'작업 등록 실패: {error_msg}'
                context['user_text_input'] = user_input
        else:
            context['error'] = "입력 내용이 없습니다."

    return render(request, 'input_form.html', context)



