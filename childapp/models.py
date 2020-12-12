from django.db import models
from datetime import datetime

#Create your models here.
class Post(models.Model):
    sno = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=200)
    date_published = models.DateField("date published", default=datetime.now)
    draft = models.TextField()
    thumbnail = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.title

class Contactus(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=13)
    email = models.CharField(max_length=39)
    message = models.TextField(max_length=300)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return ("message from -" + self.email)



