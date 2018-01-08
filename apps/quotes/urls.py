from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.quotelist, name="quotelist"),
    url(r'^quotelist$', views.quotelist, name="quotelist"),

    url(r'^addquote$', views.addquote, name="addquote"),
    url(r'^addfav$', views.addfav, name="addfav"),
    url(r'^removefav$', views.removefav, name="removefav"),

    url(r'^(?P<id>\d+)/memberquotes$', views.memberquotes, name="memberquotes"),

    url(r'^logout$', views.logout, name="logout"),
]
