from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from bookmark.models import Bookmark


class BookmarkList(ListView):  # bookmark_list.html
    model = Bookmark


class BookmarkCreateView(CreateView):  # bookmark-form.html
    model = Bookmark
    fields = ['site_name', 'url'] #<form>
    template_name_suffix = '_create'  # bookmark_create.html -->이름 바꾸기
    success_url = reverse_lazy('bookmark:list') #db에 저장된 후에 보여주기


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    #success_url = reverse_lazy('bookmark:list')

