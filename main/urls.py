"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^', include("apps.logreg.urls")),
    url(r'^', include("apps.board.urls")),
    url(r'^logreg/', include("apps.logreg.urls")),
    url(r'^manager/', include("apps.manager.urls")),
    url(r'^board/', include("apps.board.urls")),
    url(r'^chat/', include("apps.chat.urls")),
    url(r'^quotes/', include("apps.quotes.urls")),
    url(r'^rest/', include("apps.rest.urls")),

]
