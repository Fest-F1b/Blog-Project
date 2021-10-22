"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django import contrib
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import login
from django.urls import is_valid_path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
<<<<<<< HEAD
    path('', include("django.contrib.auth.urls")),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html')),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html')),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'), name='password-reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password-reset_done.html'), name='password_reset/done'),
    path(
        'password-reset-confirm/<uidb64>/ <token>',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password-reset_confirm.html'), name='password_reset_confirm'),
    path('', include('blogApp.urls')),

=======
    path('', include('blogApp.urls'))
<<<<<<< HEAD
=======

>>>>>>> fbc4e48c5a973e4301bd1924a9f9249946f9b4f5
>>>>>>> 7a219ca7f53d796c422471c6d1f970675bbae3bb
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Fester Blog Administration"
admin.site.site_title = "festerm Admin"
admin.site.index_title = "festerm"
