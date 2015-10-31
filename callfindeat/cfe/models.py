from django.db import models

# Create your models here.
class t_admin(models.Model):
    level = models.IntegerField(max_length=11)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    realname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

class t_cash(models.Model):
    amount = models.FloatField(max_length=255)
    cfrom = models.BigIntegerField(max_length=20)
    cto = models.BigIntegerField(max_length=20)
    date = models.CharField(max_length=255)
    state = models.IntegerField(max_length=11)

class t_contractsite(models.Model):
    content = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    state = models.IntegerField(max_length=11)

class t_customer(models.Model):
    address = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    pid = models.ForeignKey(t_position)

class t_deliver(models.Model):
    age = models.IntegerField(max_length=11)
    isWork = models.IntegerField(max_length=11)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    pid = models.ForeignKey(t_position)

class t_ensurance(models.Model):
    level = models.IntegerField(max_length=11)
    money = models.FloatField(max_length=255)
    rid = models.ForeignKey(t_restaurant)
    sid = models.ForeignKey(t_site)

class t_evluatercrd(models.Model):
    id = models.ForeignKey(t_deliver, t_customer)
    content = models.CharField(max_length=255)
    level = models.IntegerField(max_length=11)
    cid = models.ForeignKey(t_customer)
    did = models.ForeignKey(t_deliver)
    time = models.CharField(max_length=255)

class t_food(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    rid = models.BigIntegerField(max_length=20)

class t_of(models.Model):
    quantity = models.IntegerField(max_length=11)
    fid = models.ForeignKey(t_food)
    oid = models.ForeignKey(t_order)

class t_order(models.Model):
    price = models.FloatField(max_length=255)
    state = models.IntegerField(max_length=11)
    cid = models.ForeignKey(t_customer)
    rid = models.ForeignKey(t_task)
    sid = models.ForeignKey(t_site)
    time = models.CharField(max_length=255)
    tid = models.ForeignKey(t_restaurant)

class t_position(models.Model):
    refer = models.CharField(max_length=255)
    type = models.IntegerField(max_length=11)
    x = models.IntegerField(max_length=11)
    y = models.IntegerField(max_length=11)

class t_restaurant(models.Model):
    address = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    pid = models.ForeignKey(t_position)

class t_salary(models.Model):
    basic = models.FloatField(max_length=255)
    month = models.IntegerField(max_length=11)
    other = models.FloatField(max_length=255)
    prize = models.FloatField(max_length=255)
    did = models.ForeignKey(t_deliver)

class t_site(models.Model):
    host = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    csid = models.ForeignKey(t_contractsite)

class t_task(models.Model):
    distance = models.FloatField(max_length=255)
    path = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    did = models.ForeignKey(t_deliver)

