from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# # Create your views here.
# class HomeView(TemplateView):
#     template_name = 'home.html'

class PostView(ListView):
    template_name = 'home.html'
    model=Post

class PostDetailsViewsp(DetailView):
    template_name = 'detail.html'
    model = Post

