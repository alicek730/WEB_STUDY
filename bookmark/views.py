from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

class BookmarkLV(ListView): # 템플릿 파일명을 bookmark_list.html로 설정
    model = Bookmark

class BookmarkDV(DetailView):  # 템플릿 파일명을 bookmark_detail.html로 설정
    model = Bookmark
