from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Content, name = 'contentPage'), # URL to Landing Page
]
