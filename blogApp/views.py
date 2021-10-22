from django.db import models
from django.db.models import fields
from django.db.models.aggregates import Count
from django.db.models.expressions import F
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView,ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import DeleteView
from .models import Category_post, Comment, Post
from .forms import CommentForm, SubscribeForm
from users.models import Profile
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
import datetime


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')[:6]
    template_name = 'blogapp/index.html'
    paginate_by = 5


def latest_list(request):
    latest_list = Post.objects.filter(created_on__month=9).order_by('-created_on')[:3]
    context = {
        "latest_list": latest_list,
    }
    return context


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
     context = {
          "la_posts":la_posts,
     }
     return context


class CatListView(ListView):
     template_name = 'blogapp/category.html'
     context_object_name = 'catlist'
     
     def get_queryset(self):
          content = {
          'cat':self.kwargs['category'],
          'posts':Post.objects.filter(category__name = self.kwargs['category']).filter(status=1)

          }
          return content


def category_list(request):
     category_list = Category_post.objects.exclude(name="default")
     context ={
          "category_list": category_list,
     }
     return context


# PROFILE VIEW
# view for user profile page
def profp(request):
    userp = Profile.objects.all()
    return render(request, 'blogapp\profile.html', ({'userp': userp}))
