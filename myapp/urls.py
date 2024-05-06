from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('project/', views.project),
    path('task/', views.task),
]