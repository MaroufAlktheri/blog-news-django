from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Posts

class PostsListView(ListView):
    model = Posts



class PostDetailView(DetailView):
    model = Posts