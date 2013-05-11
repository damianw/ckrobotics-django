from django.db import models

LEAGUETYPE = (
    ('v', 'VEX'),
    ('f', 'FTC'),
    ('l', 'FLL'),
    ('i', 'VEXIQ'),
)

LEAGUEMATCH = dict((x, y) for x, y in LEAGUETYPE)

class Description(models.Model):
  name = models.CharField(max_length=20)
  text = models.CharField(max_length=65535)

class CompetitionGame(models.Model):
	name = models.CharField(max_length=20)
	season_start = models.DateField()
	season_end = models.DateField()
	league = models.CharField(max_length=1, choices=LEAGUETYPE)
	current = models.BooleanField()
	description = models.CharField(max_length=65535)
	teams = models.CharField(max_length=65535)
	rules = models.CharField(max_length=65535)

class BlogPost(models.Model):
	title = models.CharField(max_length=20)