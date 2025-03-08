from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation_home, name='documentation_home'),
]