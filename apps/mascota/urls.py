from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'mascota'

urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^lista', views.lista, name='lista')
    #url(r'^create', views.create, name='create'),
    #url(r'^editar/(?P<id_mascota>\d+)/$', views.edit, name='editar'),
    #url(r'^eliminar/(?P<id_mascota>\d+)/$', views.delete, name='eliminar'),
    url(r'^vacuna', views.vacuna, name='vacuna'),


    url(r'^lista', views.MascotaList.as_view(), name='lista'),
    url(r'^create', views.MascotaCreate.as_view(), name='create'),
    url(r'^editar/(?P<pk>\d+)/$', views.MascotaUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.MascotaDelete.as_view(), name='eliminar'),

    #path('', views.create_vacuna, name='create_vacuna')
]
