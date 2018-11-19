from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'new^$', views.new),
    url(r'^create$', views.add),
    url(r'^(?P<num>\d+)$', views.project),
    url(r'^(?P<num>\d+)/vote$', views.vote),
    url(r'^(?P<num>\d+)/update$', views.add_vote),
]