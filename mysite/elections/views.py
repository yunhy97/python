from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# index 함수에 요청이 오면 return 값을 실행
def index(request):
    return HttpResponse("Hello World~~")