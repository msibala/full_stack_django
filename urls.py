from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^post$', views.post),
    url(r'^comment$', views.comment),
    url(r'^logout$', views.logout),
    url(r'^delmsg/(?P<id>[0-9]+)$', views.delmsg),
    url(r'^delcom/(?P<id>[0-9]+)$', views.delcom),



]