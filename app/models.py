from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=20)
    viewPassword=models.CharField(max_length=200,null=True)

class User(models.Model):
    user= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20,null=True)
    Image=models.ImageField(upload_to="Image",null=True)
    Address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=20,default='pending')

class Ambassador(models.Model):
    ambassador= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20,null=True)
    Image=models.ImageField(upload_to="Image",null=True)
    Address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=20,default='pending')

class Guide(models.Model):
    guide= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20,null=True)
    Image=models.ImageField(upload_to="Image",null=True)
    Address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=20,default='pending')

class Event(models.Model):
    ambassador= models.ForeignKey(Ambassador,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    date=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to="Image",null=True)
    des=models.CharField(max_length=200,null=True)
    dis=models.CharField(max_length=200,null=True)

class Book(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(null=True)
    dist=models.CharField(max_length=200,null=True)
    rate=models.IntegerField(null=True)
    event= models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    guide= models.ForeignKey(Guide,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')

class Chat(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    guideid = models.ForeignKey(Guide, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)

class Article(models.Model):
    ambassador= models.ForeignKey(Ambassador,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True,null=True)
    image=models.ImageField(upload_to="Image",null=True)
    des=models.CharField(max_length=200,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=20,default='pending')
    reply=models.CharField(max_length=200,null=True)
    ambassador= models.ForeignKey(Ambassador,on_delete=models.CASCADE,null=True)
    article= models.ForeignKey(Article,on_delete=models.CASCADE,null=True)

class Service(models.Model):
    guide= models.ForeignKey(Guide,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    sdate=models.DateField(null=True)
    edate=models.DateField(null=True)
    rate=models.IntegerField(null=True)
    image=models.ImageField(upload_to="Image",null=True)
    food=models.CharField(max_length=200,null=True)
    dis=models.CharField(max_length=200,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    guide= models.ForeignKey(Guide,on_delete=models.CASCADE,null=True)
    service= models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')

class Events(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    date=models.DateField(null=True)
    image=models.ImageField(upload_to="Image",null=True)
    ename=models.CharField(max_length=200,null=True)
    dis=models.CharField(max_length=200,null=True)
    des=models.CharField(max_length=200,null=True)
    fee=models.IntegerField(null=True)
    status=models.CharField(max_length=20,default='pending')

class Registered(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')
    events=models.ForeignKey(Events,on_delete=models.CASCADE,null=True)

class Chats(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    ambassadorid = models.ForeignKey(Ambassador, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)

