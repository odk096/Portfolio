from django.db import models

# Create your models here.


class Previous_work(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='previous_work/')
    website = models.CharField(max_length=500, blank=True, null=True)

class profile_pic(models.Model):
    image = models.ImageField(upload_to='profile_pic/')

class CV(models.Model):
    file = models.FileField(upload_to='cv/')

class contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)