from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Author
from .serializers import ArticleSeiralizer


class ArticleView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        ser = ArticleSeiralizer(articles,many=True) 
        return Response({"articles":ser.data})


    def post(self,request):
        articles = request.data.get('articles')
        ser = ArticleSeiralizer(data=articles)
        if ser.is_valid(raise_exception=True):
            art = ser.save()
        return Response({"added":"Article {} added".format(art.title)})    