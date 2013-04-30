from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from teams.models import Team

def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_poll_list': latest_poll_list}
    context = {'team_list': Team.objects.all()}
    return render(request, 'teams/index.html', context)

def detail(request, poll_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'teams/detail.html', {'team': team})