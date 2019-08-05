from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm, VacunaForm
from apps.mascota.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	return render(request , 'mascota/index.html' )


def create(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)

		if form.is_valid():
			form.save()
		return redirect('mascota:lista')

	else:
		form = MascotaForm()

	return render(request, 'mascota/create.html', {'form' : form})


def edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance = mascota)
	else:
		form = MascotaForm(request.POST, instance = mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:lista')
	return render(request, 'mascota/create.html', {'form' : form})


def delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:lista')
	return render(request, 'mascota/delete.html', {'mascota' : mascota})


def vacuna(request):
	if request.method == 'POST':
		form = VacunaForm(request.POST)

		if form.is_valid():
			form.save()
		return redirect('mascota:index')

	else:
		form = VacunaForm()

	return render(request, 'mascota/create_vacuna.html', {'form' : form})


def lista(request):
	mascotas = Mascota.objects.all()
	context = {'mascotas' : mascotas}

	return render(request, 'mascota/lista.html', context)


class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/lista.html'


class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/create.html'
	success_url = reverse_lazy('mascota:lista')

class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/create.html'
	success_url = reverse_lazy('mascota:lista')

class MascotaDelete(DeleteView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/delete.html'
	success_url = reverse_lazy('mascota:lista')