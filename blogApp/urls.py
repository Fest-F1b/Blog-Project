from os import name
from .import views
from django.urls import path
<<<<<<< HEAD
from django.views.decorators.cache import cache_page
=======
>>>>>>> fbc4e48c5a973e4301bd1924a9f9249946f9b4f5

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('l_view', views.l_view, name='l_view'),
<<<<<<< HEAD
    path('category/<category>', views.CatListView.as_view(),name='category'),
    path('profp', views.profp, name='profp'),

=======
<<<<<<< HEAD
    path('category/<category>', views.CatListView.as_view(),name='category')
>>>>>>> 7a219ca7f53d796c422471c6d1f970675bbae3bb


]
=======
    path('category', views.category, name='category'),
    

    


]
>>>>>>> fbc4e48c5a973e4301bd1924a9f9249946f9b4f5
