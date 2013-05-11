from django.db import models
from django.contrib.auth.models import User, Group
from blog.models import LEAGUETYPE, LEAGUEMATCH

class Robot(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)

class Team(Group):
	def generate_name(self):
		return str(self.league) + str(self.teamname) + str(self.number)
	def save(self, *args, **kwargs):
		if not self.name:
			self.name = self.generate_name()
		super(Team, self).save(*args, **kwargs)
	def __unicode__(self):
		return LEAGUEMATCH[self.league] + ' ' + str(self.number) + ' ' + str(self.teamname)
	teamname = models.CharField(max_length=50)
	number = models.IntegerField()
	founded_date = models.DateField()
	league = models.CharField(max_length=1, choices=LEAGUETYPE)
	robots = models.ManyToManyField(Robot, blank=True)

class Member(models.Model):
	user = models.OneToOneField(User)
	join_date = models.DateField()
	current = models.BooleanField()
	grad_year = models.IntegerField()