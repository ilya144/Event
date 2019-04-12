from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=15,unique=True)

class Event(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField()
	description = models.TextField()
	tags = models.ManyToManyField(Tag)
	duration = models.DateTimeField()
	coords = models.CharField(max_length=255,unique=True)

class User(models.Model):
	name = models.CharField(max_length=25,unique=True)
	age = models.IntegerField()
	sex = models.BooleanField()#True - male, False - female
	tags = models.ManyToManyField(Tag)
	number = models.CharField(max_length=11,unique=True)
	fullname = models.TextField()
	city = models.TextField()
	password = models.CharField(max_length=20)


