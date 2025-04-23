from django.urls import path
from . import views



app_name = 'api'



urlpatterns = [
    path('tasks/', views.TaskCreateAPIView.as_view(), name='task-create'),
]
