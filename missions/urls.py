from django.urls import path
from . import views

urlpatterns = [
    path('', views.mission_list, name='mission_list'),
    path('my/', views.my_missions, name='my_missions'),
    path('<int:pk>/', views.mission_detail, name='mission_detail'),
]
