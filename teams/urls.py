from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
  # ex: /teams/
  url(r'^$', views.index, name='index'),
  # ex: /teams/5/
  url(r'^(?P<team_id>\d+)/$', views.detail, name='detail'),
)