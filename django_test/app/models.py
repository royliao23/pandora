from django.db import models
import uuid


import datetime


class Album(models.Model):
    artist = models.CharField(max_length=200, blank=False)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

# Create your models here.
class Employees(models.Model):
	firstname=models.CharField(max_length=10)
	lastname=models.CharField(max_length=10)
	emp_id=models.IntegerField()
	"""docstring for Employees"""
	def __str__(self):
		return self.firstname

class People(models.Model):
    #_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    _id = models.CharField(max_length=255)
    index = models.IntegerField(primary_key=True)
    guid = models.CharField(max_length=255)
    has_died = models.BooleanField(max_length=20)
    balance = models.FloatField()
    picture = models.CharField(max_length=255)
    age = models.IntegerField()
    eyecolor = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    company_id = models.IntegerField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    about = models.CharField(max_length=2000)
    registered = models.DateField(max_length=100)
    tags = models.TextField(null=True)
    #friends = models.ManyToManyField(to='self', related_name='flist', symmetrical=False)
    friends = models.IntegerField()
    greeting = models.TextField(max_length=300)
    favoritefoods = models.TextField(null=True)
    
class Company_Staff(models.Model):
    
    company = models.CharField(max_length=255)
    index = models.ForeignKey(People, on_delete=models.CASCADE)
    def __str__(self):
        return self.company
class Friend_List(models.Model):
    key=models.IntegerField()
    friends = models.TextField(blank=True,null=True)
    
   





 
  