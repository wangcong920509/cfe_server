__author__ = 'wangcong15'
from django.conf.urls import include, url
from django.contrib import admin

from callfindeat.view import hello, current_time, get_json, login

urlpatterns = [
    url('^hello/$', hello),
    url('^current_time/$', current_time),
    url('^getjson/$', get_json),
    url('^login/$', login),
]