from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from ckrobotics_django import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ckrobotics_django.views.home', name='home'),
    # url(r'^ckrobotics_django/', include('ckrobotics_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^teams/', include('teams.urls', namespace="teams")),
    url(r'^$', views.index, name="index"),
    url(r'^memberhome/', views.memberhome, name="memberhome"),
    url(r'^vex/', views.vex, name="vex"),
    url(r'^logout/', views.logout_view, name="logout"),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if not settings.DEBUG:
  urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
  )