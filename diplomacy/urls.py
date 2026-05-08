from django.urls import path
from . import views

urlpatterns = [
    path('', views.faction_list, name='faction_list'),
    path('faction/<int:pk>/', views.faction_detail, name='faction_detail'),
    path('planets/', views.planet_list, name='planet_list'),
    path('planets/<int:pk>/', views.planet_detail, name='planet_detail'),
]
