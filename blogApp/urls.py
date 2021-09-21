from os import name
from .import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('l_view', views.l_view, name='l_view'),
    path('category', views.category, name='category'),
    

    


]