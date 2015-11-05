__author__ = 'wangcong15'
from django.conf.urls import include, url
from django.contrib import admin

from callfindeat.view import hello, current_time, get_json, login, all_task, finished_work, finish_current, new_task

urlpatterns = [
    url('^hello/$', hello),
    url('^current_time/$', current_time),
    url('^getjson/$', get_json),
    url('^login/$', login),
    url('^all_task/', all_task),
    url('^finished_work/', finished_work),
    url('^finish_current/', finish_current),
    url('^new_task/', new_task),
]