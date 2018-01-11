from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^$', views.library, name="library"),
    url(r'^library$', views.library, name="library"),
    url(r'^allauthors$', views.allauthors, name="allauthors"),
    url(r'^new$', views.new, name="new_author"),
    url(r'^create$', views.create, name="create"),
    url(r'^(?P<id>\d+)$', views.show, name="show"),
    url(r'^(?P<id>\d+)/edit$', views.edit, name="edit"),
    url(r'^(?P<id>\d+)/edit_author$', views.edit_author, name="edit_author"),
    url(r'^(?P<id>\d+)/delete$', views.delete, name="delete"),
    url(r'^(?P<id>\d+)/delete_author$', views.delete_author, name="delete_author"),
    url(r'^likeauthor$', views.likeauthor, name="likeauthor"),    


    url(r'^works$', views.all_works, name="all_works"),

    url(r'^works/new$', views.new_work, name="new_work"),
    url(r'^works/create$', views.create_work, name="create_work"),

    url(r'^works/(?P<workid>\d+)/show$', views.show_work, name="show_work"),
    url(r'^(?P<id>\d+)/works$', views.show_author_work, name="show_author_work"),

    url(r'^works/(?P<workid>\d+)/edit$', views.worksedit, name="worksedit"),
    url(r'^works/edit_work$', views.edit_work, name="edit_work"),

    url(r'^works/(?P<workid>\d+)/delete$', views.worksdelete, name="worksdelete"),
    url(r'^works/(?P<workid>\d+)/delete_work$', views.delete_work, name="delete_work"),

    url(r'^works/addcomment$', views.addcomment, name="addcomment"),
    url(r'^works/addreply$', views.addreply, name="addreply"),

    url(r'^works/likework$', views.likework, name="likework"),

    url(r'^logout$', views.logout, name="logout"),
]
