from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

import boardApp
from boardApp import views
from boardApp.views import post_main

# router = routers.DefaultRouter()
# router.register('main/', views.post_main)


urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('', include(router.urls)),
    # path('', views.post_main),
    # path('', views.post_main.as_view(), name='board_main'),
    # path('detail/<int:id>/', views.post_detail.as_view(), name='board_detail'),
    # path('detail/<int:id>/update', views.post_update.as_view(), name='board_update'),
    # path('detail/<int:id>/delete', views.post_delete.as_view(), name='board_delete'),
    #  path('create/', views.post_create.as_view(), name='board_create'),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)