from django.urls import path
from . import views



app_name = 'core'



urlpatterns = [
    path('', views.task_input_view, name='task_input'),
]
