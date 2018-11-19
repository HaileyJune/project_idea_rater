from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'new^$', views.new),
    url(r'^create$', views.add),
    url(r'^(?P<num>\d+)$', views.project),
    url(r'^(?P<num>\d+)/edit$', views.edit),
    url(r'^(?P<num>\d+)/update$', views.update),
    url(r'^(?P<num>\d+)/vote$', views.add_vote),
]