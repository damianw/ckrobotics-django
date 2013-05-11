from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from teams.models import Team
from blog.models import Description
from django.contrib.auth.decorators import login_required

partners = ["Youthville Detroit", "Someone Else",]

def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'ckrobotics_django/test.html', {'loggedin': True})
				else:
					return render(request, 'ckrobotics_django/test.html', {'loggedin': False})
		else:
			return render(request, 'ckrobotics_django/test.html', {'loggedin': False})
	else:
		data = {'teams': Team.objects.all(),
						'partners': partners,
						'title': "CK Robotics",
						'page': 'index',
						# 'hero_unit_header': Description.objects.get(name__exact="hero_unit_header").text,
						# 'hero_unit_text': Description.objects.get(name__exact="hero_unit_text").text,
						}
		return render(request, 'ckrobotics_django/index.html', data)

def vex(request):
	data = {'teams': Team.objects.all(),
					'partners': partners,
					'title': 'About VEX',
					'page': 'vex',
					}
	return render(request, 'ckrobotics_django/vex.html', data);

@login_required(login_url='/')
def memberhome(request):
	data = {'teams': request.user.member.teams.all()}
	return render(request, 'ckrobotics_django/memberhome.html', data)