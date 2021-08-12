
from django.urls import path, include
from . import views

urlpatterns = [
    # views.py에 명시한 index 함수에 return 값 표시
    path('', views.index),
]

