from django.shortcuts import render
from .models import Article
from django import template
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
