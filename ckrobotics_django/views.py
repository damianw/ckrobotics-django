from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from teams.models import Team
from blog.models import Description
from django.contrib.auth.decorators import login_required

partners = ["Youthville Detroit", "Someone Else",]

def get_data():
	data = {'teams': Team.objects.all(),
						'vex_teams': Team.objects.filter(league='v'),
						'ftc_teams': Team.objects.filter(league='f'),
						'fll_teams': Team.objects.filter(league='l'),
						'vexiq_teams': Team.objects.filter(league='i'),
						'partners': partners,
					}
	return data

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
		data = get_data()
		data.update({
						'title': "CK Robotics",
						'page': 'index',
						})
		return render(request, 'ckrobotics_django/index.html', data)

def vex(request):
	data = get_data()
	data.update({'title': 'About VEX',
					'page': 'vex',
					})
	return render(request, 'ckrobotics_django/vex.html', data);

@login_required(login_url='/')
def memberhome(request):
	data = get_data()
	data.update({ 'page': 'memberhome',
		})
	return render(request, 'ckrobotics_django/memberhome.html', data)