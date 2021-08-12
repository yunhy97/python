from django.db import models

# Create your models here.
# Django의 모델로써 동작하려면 Model을 상속받아야 함
class Candidate(models.Model):
    # name 필드 생성, 최대 길이 10
    name = models.CharField(max_length=10)
    # introduction 필드 생성, 최대 길이 없음
    introduction = models.TextField()
    # area 필드 생성, 최대 길이 15
    area = models.CharField(max_length=15)
    # party_number 필드 생성, 기본값은 1
    party_number = models.IntegerField(default=1)

    def __str__(self):