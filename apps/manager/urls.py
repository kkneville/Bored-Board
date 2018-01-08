from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="showmembers"),
    url(r'^index$', views.index, name="showmembers"),
    url(r'^(?P<id>\d+)/profile$', views.showmember, name="showmember"),
    url(r'^(?P<id>\d+)/edit$', views.editmember, name="editmember"),
    url(r'^(?P<id>\d+)/delete$', views.deletecheck, name="deletecheck"),

]
