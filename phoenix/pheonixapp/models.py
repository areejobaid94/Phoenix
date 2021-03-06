from django.db import models
# from knox.modles import AuthToten

from django.contrib.auth.models import User



class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100,default='SOME STRING')
    Bio = models.CharField(max_length=200,default='SOME STRING')
    owner = models.ForeignKey(
        User , related_name="myapp", on_delete=models.CASCADE,null = True)

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='SOME STRING')
    country = models.CharField(max_length = 100,default='SOME STRING')
    phone = models.CharField(max_length=50,default='SOME STRING')
    image = models.CharField(max_length=500,default='SOME STRING')
    rating = models.CharField(max_length=200,default='SOME STRING')
    price = models.CharField(max_length=200,default='SOME STRING')
    desc = models.CharField(max_length=500,default='SOME STRING')
    link = models.CharField(max_length=900,default='SOME STRING')



class Blogs(models.Model):
    ProfileId = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100,default='SOME STRING')
    country = models.CharField(max_length=100,default='SOME STRING')
    Blog = models.TextField(blank=True)
    image = models.CharField(max_length=500,default='SOME STRING')



