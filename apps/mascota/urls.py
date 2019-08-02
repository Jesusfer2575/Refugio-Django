from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'mascotas'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^create', views.create, name='create')
]
