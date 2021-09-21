from django.db import models
from django.db.models import fields
from django.db.models.aggregates import Count
from django.db.models.expressions import F
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import DeleteView
from .models import Comment, Post
from .forms import CommentForm, SubscribeForm
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
import datetime


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:6]
    template_name = 'blogapp/index.html'
    paginate_by = 5


def post_detail(request, slug):
     template_name = 'blogapp/post_detail.html'
     post = get_object_or_404(Post, slug=slug)
     comments = post.comments.filter(active=True)
     new_comment = None

     # Posting subscribe email
     if request.method == 'POST':
          subscriber_form = SubscribeForm(data=request.POST)
          if subscriber_form.is_valid():
               subscriber = subscriber_form.save(commit=False)
               subscriber.save()
               messages.success(request, f'Subscribed')
     else:
          subscriber_form = SubscribeForm()

     #   for the Comments
     if request.method == 'POST':
          comment_form = CommentForm(data=request.POST)
          if comment_form.is_valid():
               new_comment = comment_form.save(commit=False)
               new_comment.post = post
               new_comment.save()

     else:
          comment_form = CommentForm()
     return render(request, template_name, {'subscriber_form': subscriber_form, 'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def l_view(request):
    la_posts = Post.objects.filter(
        created_on__month=9).order_by('-created_on')[:6]
    return render(request, "blogapp/latest.html", {'la_posts': la_posts})


def category(request):
     cat_posts = Post.objects.filter(post_in_category=all,status =1).order_by('-created_on')[:6]
     template_name = 'blogapp/category.html'
     return render (request,template_name,{'cat_posts':cat_posts})
     
