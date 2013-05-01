from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from robots.models import Robot

def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_poll_list': latest_poll_list}
    context = {'robot_list': Robot.objects.all()}
    return render(request, 'robots/index.html', context)

def detail(request, robot_id):
    robot = get_object_or_404(Robot, pk=robot_id)
    return render(request, 'robots/detail.html', {'robot': robot})