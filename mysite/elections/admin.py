from django.contrib import admin
from .models import Candidate

# Register your models here.
# models.py에 명시한 class Candidate를 사용할 것을 명시
admin.site.register(Candidate)
