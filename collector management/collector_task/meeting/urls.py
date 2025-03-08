from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventPageView, name='calender'),
    path('data/', views.DataView, name='data'),
    path('delete-events/', views.delete_events, name='delete-events'),
    path('input/',views.EventRegisterView, name='input'),
]
