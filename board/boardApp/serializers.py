from rest_framework import serializers
from boardApp.models import Post

'''
Rest Framework에서는 serializer로
Model로부터 가져온 데이터베이스의 데이터들을 JSON이나 XML같은 형식으로 쉽게 변환할 수 있게 도와줌
가져온 데이터를 가공하여 사용자의 요청에 응답
'''
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'id', 'content', 'title','author','regdate')

