from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.log_reg),
    url(r'^register$', views.reg),
    url(r'^login$', views.log),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]