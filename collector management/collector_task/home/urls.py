from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('announcement/', views.announcement_redirect, name='announcement_redirect'),
    path('task-tracker/', views.task_tracker_redirect, name='task_tracker_redirect'),
    path('ai-prediction/', views.ai_prediction_redirect, name='ai_prediction_redirect'),
    path('ai-documentation/', views.ai_documentation_redirect, name='ai_documentation_redirect'),
    path('meeting-scheduler/', views.meeting_scheduler_redirect, name='meeting_scheduler_redirect'),
    path('logout/', views.logout_view, name='logout'),
]
