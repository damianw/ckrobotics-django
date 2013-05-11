from django.db import models
from django.contrib.auth.models import User, Group
from teams.models import Team, LEAGUETYPE, LEAGUEMATCH

class Description(models.Model):
  name = models.CharField(max_length=20)
  text = models.TextField()

class CompetitionGame(models.Model):
	name = models.CharField(max_length=20)
	season_start = models.DateField()
	season_end = models.DateField()
	league = models.CharField(max_length=1, choices=LEAGUETYPE)
	current = models.BooleanField()
	description = models.TextField()
	teams = models.TextField()
	rules = models.TextField()

class BlogPost(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.ForeignKey(User, blank=True, null=True)
	teamauthor = models.ForeignKey(Team, blank=True, null=True)
	pub_date = models.DateTimeField()