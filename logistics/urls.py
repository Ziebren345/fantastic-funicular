from django.urls import path
from . import views

urlpatterns = [
    path('', views.gear_request_list, name='gear_request_list'),
    path('new/', views.gear_request_create, name='gear_request_create'),
    path('<int:pk>/', views.gear_request_detail, name='gear_request_detail'),
]
