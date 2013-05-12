from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404
from teams.models import Team
from blog.models import Description
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

partners = ["Youthville Detroit", "Someone Else",]

def get_data():
	data = {'teams': Team.objects.all(),
						'vex_teams': Team.objects.filter(primarygroup=Group.objects.get(name='VEX')),
						'ftc_teams': Team.objects.filter(primarygroup=Group.objects.get(name='FTC')),
						'fll_teams': Team.objects.filter(primarygroup=Group.objects.get(name='FLL')),
						'vexiq_teams': Team.objects.filter(primarygroup=Group.objects.get(name='VEXIQ')),
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

def logout_view(request):
	logout(request)
	return redirect('/')

@login_required(login_url='/')
def memberhome(request):
	data = get_data()
	data.update({ 'page': 'memberhome',
		})
	return render(request, 'ckrobotics_django/memberhome.html', data)