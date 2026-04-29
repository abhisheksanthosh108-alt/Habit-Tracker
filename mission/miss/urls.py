from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='home'),
    path('tracker/', views.tracker, name='tracker'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
]