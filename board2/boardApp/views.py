import json

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from boardApp.models import Board


# 게시판 목록 정보 json
@csrf_exempt
def list(request):
    boards = Board.objects.all().order_by('-id')
    board_list = serializers.serialize('json', boards)
    return HttpResponse(board_list, content_type="text/json-comment-filtered")


# 게시판 목록 페이지 연결
def listView(request):
    return render(request, 'board_list.html')


# 게시물 생성 정보 저장
@csrf_exempt
def create(request):
    board = Board(
        title=request.POST['title'],
        content=request.POST['content'],
        author=request.POST['author'],
    )
    board.save()
    return redirect('/boardView/')


# 게시물 생성 페이지 연결
def createView(request):
    return render(request, 'board_form.html')


# 게시물 상세 조회 정보 json
# pk로 해당 게시물 정보를 조회
def detail(request, pk):
    boards = Board.objects.filter(pk=pk)
    board_detail = serializers.serialize('json', boards)
    return HttpResponse(board_detail, content_type="text/json-comment-filtered")


# 게시물 상세 조회/수정/삭제 페이지
def detailView(request, pk):
    context = {'pk': pk}
    return render(request, 'board_detail.html', context)


# 게시물 수정 정보 저장
# pk에 해당하는 게시물 정보를 수정
@csrf_exempt
def update(request, pk):
    board = Board.objects.get(pk=pk)

    board.title = request.POST['title']
    board.content = request.POST['content']
    board.author = request.POST['author']
    board.save()
    return redirect('/detailView/' + str(board.pk))


# 게시물 삭제 정보
# pk에 해당하는 게시물 정보 삭제
@csrf_exempt
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boardView/')
