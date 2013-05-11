from django.db import models
from django.contrib.auth.models import User
from blog.models import LEAGUETYPE

class Team(models.Model):
  name = models.CharField(max_length=200)
  number = models.IntegerField(max_length=200)
  founded_date = models.DateField()
  league = models.CharField(max_length=1, choices=LEAGUETYPE)

  def __unicode__(self):
  	return self.name

class Member(models.Model):
	user = models.OneToOneField(User)
	teams = models.ManyToManyField(Team)
	join_date = models.DateField()
	current = models.BooleanField()
	grad_year = models.IntegerField()

class Robot(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)
	teams = models.ManyToManyField(Team)