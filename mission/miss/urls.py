from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('tracker/', views.home, name='home'),

    path('add/', views.add, name='add'),
    path('track/', views.track, name='track'),
    path('stay/', views.stay, name='stay'),
    path('toggle/<int:id>/', views.toggle, name='toggle'),
    path('about/', views.about, name='about'),
]