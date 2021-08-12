from rest_framework import routers
from boardApp import views

'''
Rest Framework에서는 자동으로 라우팅하는 기능 제공
사용자의 요청을 확인하고 어디에서 요청이 처리되어야 하는지 알려줌
'''
router = routers.DefaultRouter()
router.register('main', views.post_main)
