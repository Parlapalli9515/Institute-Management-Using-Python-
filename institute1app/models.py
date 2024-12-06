from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
class Commet(models.Model):
    commit=models.CharField(max_length=9050)

class Coursedetails(models.Model):
    course_no = models.IntegerField()
    course_name = models.CharField(max_length=50)
    course_fee=models.BigIntegerField()
    duration=models.CharField(max_length=50)
    start_date=models.DateField()
    start_time=models.TimeField()
    trainer_name=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
