from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from teams.models import Team
from blog.models import Description

partners = ["Youthville Detroit", "Someone Else",]

def index(request):
	homepage = {'title': "CK Robotics",
		'teams': Team.objects.all(),
		'hero_unit_header': Description.objects.get(name__exact="hero_unit_header").text,
		'hero_unit_text': Description.objects.get(name__exact="hero_unit_text").text,
		'partners': partners, }
	return render(request, 'ckrobotics_django/index.html', {'homepage': homepage})
