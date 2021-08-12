"""board2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from boardApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 게시판 목록 관련 URL
    path('boardList/', views.list, name='list'),
    path('boardView/', views.listView, name='listView'),
    # 게시물 생성 관련 URL
    path('boardCreate/', views.create, name='create'),
    path('createView/', views.createView, name='createView'),
    # 게시물 상세 조회 관련 URL
    path('boardDetail/<int:pk>/', views.detail, name='detail'),
    # 게시물 수정 관련 URL
    path('boardUpdate/<int:pk>/', views.update, name='update'),
    # 게시물 삭제 관련 URL
    path('boardDelete/<int:pk>/', views.delete, name='delete'),
    path('detailView/<int:pk>/', views.detailView, name='detailView'),

]
