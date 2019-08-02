from django.conf.urls import url, include

from . import views

app_name = 'adopcion'


urlpatterns = [
	url(r'^$', views.index),
	url(r'^create', views.create, name='create')
]