from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class post_main(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BoardView(TemplateView):
    template_name: str = 'post_list.html'


class BoardDetailView(TemplateView):
    template_name: str = 'post_detail.html'


class BoardFormView(TemplateView):
    template_name: str = 'post_form.html'
