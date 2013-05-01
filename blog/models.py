from django.db import models

class Description(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=65535)