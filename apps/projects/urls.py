from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^new$', views.new),
    url(r'^(?P<id>\d+)$', views.project),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/update$', views.update),
    url(r'^(?P<id>\d+)/vote$', views.add_vote),
]