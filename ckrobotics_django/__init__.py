from django.db import models
from django.contrib.auth.models import User, Group
Group.add_to_class('league', models.BooleanField())