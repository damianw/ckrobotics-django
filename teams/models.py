from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=5)
    #creation_date = models.DateTimeField('date published')