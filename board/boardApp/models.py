from django.contrib.auth.models import User
from django.db import models

# Create your models here.


'''
Post 모델 클래스 생성
작성 후 명령어 실행
    python manage.py makemigration
    python manage.py migrate
'''
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-regdate']

    def __str__(self):
        return self.title
