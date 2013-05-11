from django.db import models
from django.contrib.auth.models import User, Group
from blog.models import LEAGUETYPE

class Robot(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)

class Team(Group):
  number = models.IntegerField(max_length=200)
  founded_date = models.DateField()
  league = models.CharField(max_length=1, choices=LEAGUETYPE)
  robots = models.ManyToManyField(Robot)

class Member(models.Model):
	user = models.OneToOneField(User)
	join_date = models.DateField()
	current = models.BooleanField()
	grad_year = models.IntegerField()