from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventList.as_view()),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/$', views.EventDetail.as_view()),
    url(r'^search/$', views.EventSearch.as_view()),
]