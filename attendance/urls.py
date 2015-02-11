from django.conf.urls import patterns, url

from attendance import views

urlpatterns = patterns('',
    url(r'^(?P<course>[a-zA-Z0-9]{6})/$', views.index, name='index'),
    url(r'^(?P<course>[a-zA-Z0-9]{6})/success/$',views.success, name='success'),
    url(r'^(?P<course>[a-zA-Z0-9]{6})/failed/$',views.failed, name='failed')
)