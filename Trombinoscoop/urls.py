"""Trombinoscoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Trombinoscoop.views import welcome, login, register, add_friend, show_profile, modify_profile
from .views import ajax_check_email_field, ajax_add_friend

urlpatterns = [
    url('^$', welcome),
    url('^welcome$', welcome),
    url('^login$', login),
    url('^register$', register),
    url('^addFriend$', add_friend),
    url('^showProfile$', show_profile),
    url('^modifyProfile$', modify_profile),
    url('^ajax/checkEmailField$', ajax_check_email_field),
    url('^ajax/addFriend$', ajax_add_friend),
    url(r'^admin/', admin.site.urls),
]
