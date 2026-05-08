from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnel_list, name='personnel_list'),
    path('me/', views.my_personnel, name='my_personnel'),
    path('<int:pk>/', views.personnel_detail, name='personnel_detail'),
]
