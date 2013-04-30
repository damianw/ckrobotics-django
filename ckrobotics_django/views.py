from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from teams.models import Team

partners = ["Youthville Detroit", "Someone Else",]
homepage = {'title': "CK Robotics", 'teams': Team.objects.all(), 'partners': partners}

def index(request):
    return render(request, 'ckrobotics_django/index.html', {'homepage': homepage})