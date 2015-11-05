__author__ = 'wangcong15'

from django.http import HttpResponse
from cfe.models import t_deliver, t_task, t_order
from datetime import datetime
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
        getadmin = t_deliver.objects.filter(phone = mphone, password = mpass)
        if(len(getadmin) == 0):
            data = {"state": 0, "desc": "Wrong Password Or Phone Number"}
        else:
            data = {"state": 1, "desc": "Correct"}
    else:
        data = {"state": 2, "desc": "Lack Of Parameters"}
    return HttpResponse(json.dumps(data, ensure_ascii=False))

def all_task(request):
    ontask = []
    finished = []
    state = 0
    if request.method == 'GET' and 'phone' in request.GET:
        mphone = request.GET['phone']
        currentdeliver = t_deliver.objects.filter(phone=mphone)
        if currentdeliver:
            currentdeliver = currentdeliver[0]
            tasklist = currentdeliver.t_task_set.all().order_by('-id')
            if tasklist:
                lastorderlist = tasklist[0].t_order_set.all()
                flag = 0
                for order in lastorderlist:
                    if order.state == 0:
                        flag = 1
                if flag == 1:
                    for order in lastorderlist:
                        ontask.append({'x':order.rid.pid.x, 'y':order.rid.pid.y, 'desc':order.rid.name})
                    for order in lastorderlist:
                        ontask.append({'x':order.cid.pid.x, 'y':order.cid.pid.y, 'desc':order.cid.address})
                else:
                    finished.append({'time':tasklist[0].time, 'desc':tasklist[0].path, 'id':tasklist[0].id})
                taskflag = 0
                for task in tasklist:
                    if taskflag == 0:
                        taskflag += 1
                        continue
                    finished.append({'time':task.time, 'desc':task.path, 'id':task.id})
            state = 1
    data = {"state": state, "on-task": ontask, "finished": finished}
    return HttpResponse(json.dumps(data, ensure_ascii=False))

def finished_work(request):
    state = 0
    orders = []
    if request.method == 'GET' and 'taskid' in request.GET:
        taskid = request.GET['taskid']
        task = t_task.objects.filter(id=taskid)
        if task:
            task = task[0]
            orderlist = task.t_order_set.all()
            for order in orderlist:
                orders.append({'id':order.id, 'price':order.price, 'restaurant':{'name':order.rid.name, 'address':order.rid.address, 'phone':order.rid.phone}, 'customer':{'name':order.cid.name, 'address':order.cid.address, 'phone':order.cid.phone}})
            state = 1
    data = {"state":state, "orders":orders}
    return HttpResponse(json.dumps(data, ensure_ascii=False))

def finish_current(request):
    state = 0
    if request.method == 'GET' and 'phone' in request.GET:
        mphone = request.GET['phone']
        deliver = t_deliver.objects.filter(phone=mphone)
        if deliver:
            deliver = deliver[0]
            tasklist = deliver.t_task_set.all().order_by('-id')
            if tasklist:
                lastorderlist = tasklist[0].t_order_set.all()
                for order in lastorderlist:
                    order.state = 1
                    order.save()
                state = 1
    data = {"state":state}
    return HttpResponse(json.dumps(data, ensure_ascii=False))

def new_task(request):
    ontask = []
    state = 0
    if request.method == 'GET' and 'phone' in request.GET:
        mphone = request.GET['phone']
        currentdeliver = t_deliver.objects.filter(phone=mphone)
        if currentdeliver:
            currentdeliver = currentdeliver[0]
            tasklist = currentdeliver.t_task_set.all().order_by('-id')
            if tasklist:
                lastorderlist = tasklist[0].t_order_set.all()
                flag = 0
                for order in lastorderlist:
                    if order.state == 0:
                        flag = 1
                if flag == 1:
                    state = 2
                    data = {"state":state, "on-task":ontask}
                    return HttpResponse(json.dumps(data, ensure_ascii=False))

            neworderlist = t_order.objects.filter(state=0, tid=None).order_by('id')
            if not neworderlist:
                state = 3
            if neworderlist:
                if len(neworderlist) < 5:
                    state = 3
                else:
                    state = 1
                    path = ''
                    ordercounter = 0
                    for order in neworderlist:
                        ordercounter += 1
                        if ordercounter > 5:
                            break
                        ontask.append({'x':order.rid.pid.x, 'y':order.rid.pid.y, 'desc':order.rid.name})
                        path += order.rid.name + ' -> '
                    ordercounter = 0
                    for order in neworderlist:
                        ordercounter += 1
                        if ordercounter > 5:
                            break
                        ontask.append({'x':order.cid.pid.x, 'y':order.cid.pid.y, 'desc':order.cid.address})
                        if ordercounter == 5:
                            path += order.cid.address
                        else:
                            path += order.cid.address + ' -> '
                    datestr = datetime.today().strftime("%Y%m%d")
                    newtask = t_task(path=path, time=datestr, did=currentdeliver)
                    newtask.save()
                    ordercounter = 0
                    for order in neworderlist:
                        order.tid = newtask
                        order.save()


    data = {"state": state, "on-task": ontask}
    return HttpResponse(json.dumps(data, ensure_ascii=False))


