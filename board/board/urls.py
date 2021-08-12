"""board URL Configuration

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
from boardApp import views
from .routers import router
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework의 urls.py를 포함
    path('api-auth/', include('rest_framework.urls')),
    # router의 urls.py를 포함
    path('api/', include(router.urls)),
    path('boardApp/', views.BoardView.as_view()),
    path('boardApp/detail/<int:id>/', views.BoardDetailView.as_view(), name="detail"),
    path('boardApp/form/', views.BoardFormView.as_view(), name="form"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
