from django.db import models
from django.contrib.auth.models import User
class Student_profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    PhoneNumber = models.CharField(max_length=250,default="")

    qualification = models.CharField(max_length=250,default="")

    subjects = models.CharField(max_length=250,default="")

    percentage = models.CharField(max_length=250,default="")

    Description = models.CharField(max_length=250,default="")

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


class Hobby_details(models.Model):

    student = models.ForeignKey('Student_profile', on_delete=models.CASCADE,null=True,blank=True)

    hobby = models.CharField(max_length=256)
