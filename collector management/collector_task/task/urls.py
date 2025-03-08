from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_home, name='task_home'),
]