__author__ = 'wangcong15'

from django.http import HttpResponse
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