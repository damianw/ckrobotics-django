from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

teams = ["35 - Unidentified", "36 - The Scrubs", "37 - Athena Rising", "38 - Vexellent", "39 - The Zip_Ties", ]
partners = ["Youthville Detroit", "Someone Else",]
homepage = {'title': "CK Robotics", 'teams': teams, 'partners': partners}

def index(request):
    return render(request, 'ckrobotics_django/index.html', {'homepage': homepage})