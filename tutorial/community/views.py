from django.shortcuts import render

# Create your views here.
from community.forms import *


def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html', {'form': form})

def list(request):
    #DB에 저장된 모든 컬럼을 담는다.
    articleList = Article.objects.all()
    return render(request, 'list.html',{'articleList': articleList})

def view(request, num="1"):
    article = Article.objcets.get(id=num)
    return render(request, 'view.html', {'article': article})