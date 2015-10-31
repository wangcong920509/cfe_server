from django.db import models

# Create your models here.
class t_admin(models.Model):
    id = models.BigIntegerField(max_length=20)
    level = models.IntegerField(max_length=11)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    realname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

class t_cash(models.Model):
    id = models.BigIntegerField(max_length=20)
    amount = models.FloatField(max_length=0)
    cfrom = models.BigIntegerField(max_length=20)
    cto = models.BigIntegerField(max_length=20)
    date = models.CharField(max_length=255)
    state = models.IntegerField(max_length=11)

class t_contractsite(models.Model):
    id = models.BigIntegerField(max_length=20)
    content = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    state = models.IntegerField(max_length=11)

class t_customer(models.Model):
    id = models.BigIntegerField(max_length=20)
    address = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    pid = models.BigIntegerField(max_length=20)

class t_deliver(models.Model):
    id = models.BigIntegerField(max_length=20)
    age = models.IntegerField(max_length=11)
    isWork = models.IntegerField(max_length=11)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    pid = models.BigIntegerField(max_length=20)

class t_ensurance(models.Model):
    id = models.BigIntegerField(max_length=20)
    age = models.IntegerField(max_length=11)
    isWork = models.IntegerField(max_length=11)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
