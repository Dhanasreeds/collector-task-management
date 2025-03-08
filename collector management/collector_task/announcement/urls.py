from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcement_home, name='announcement_home'),
]
