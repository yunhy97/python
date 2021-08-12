from django.contrib import admin

# Register your models here.
from boardApp.models import Board

# Board모델 추가 : 127.0.0.1/admin에 접속 시 Board모델이 추가된 것을 확인
admin.site.register(Board)