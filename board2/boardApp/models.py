from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# settings.py에 DATABASES에 설정된 db에 반영
# Database에 반영할 테이블과 컬럼
# class 작성 후 명령어 실행
#   python manage.py makemigrations
#   python manage.py migrate
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-regdate']

    def __str__(self):
        return self.title
