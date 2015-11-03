__author__ = 'wangcong15'

from django.http import HttpResponse
from cfe.models import t_admin
import json
import time

def hello(request):
    return HttpResponse("Hello world? This is my first trial.")

def current_time(request):
    return HttpResponse("Current time is: "+time.strftime('%Y-%m-%d %H:%M:%S'))

def get_json(request):
    if request.method == 'GET' and 'q' in request.GET:
        question = request.GET['q']
        data = {"a": question + '-->Good!'}
        #ensure_ascii=False
        return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
        return HttpResponse("Current time is: "+time.strftime('%Y-%m-%d %H:%M:%S'))

def login(request):
    if request.method == 'GET' and 'phone' in request.GET and 'pass' in request.GET:
        mphone = request.GET['phone']
        mpass = request.GET['pass']
        getadmin = t_admin.objects.filter(phone = mphone, password = mpass)
        if(len(getadmin) == 0):
            data = {"state": 0, "desc": "Wrong Password Or Phone Number"}
        else:
            data = {"state": 1, "desc": "Correct"}
    else:
        data = {"state": 2, "desc": "Lack Of Parameters"}
    return HttpResponse(json.dumps(data, ensure_ascii=False))