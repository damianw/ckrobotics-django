from django.db import models
from django.contrib.auth.models import User, Group

class Robot(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()

class Member(models.Model):
	def __unicode__(self):
		return self.user.username
	user = models.OneToOneField(User)
	join_date = models.DateField()
	current = models.BooleanField()
	grad_year = models.IntegerField()

class Team(models.Model):
	def __unicode__(self):
		return self.primarygroup.name + ' ' + str(self.number) + ' ' + str(self.name)
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	founded_date = models.DateField()
	members = models.ManyToManyField(Member, blank=True, related_name='teams')
	# league = models.CharField(max_length=1, choices=LEAGUETYPE)
	primarygroup = models.ForeignKey(Group, related_name='primaryteams')
	groups = models.ManyToManyField(Group, related_name='teams')
	robots = models.ManyToManyField(Robot, blank=True)
# Group.add_to_class('team', models.OneToOneField(Team, 
# 	related_name='group', blank=True, null=True))
# Group.team.blank=False
# Group.team.null=False
