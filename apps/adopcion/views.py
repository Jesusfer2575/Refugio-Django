from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.adopcion.forms import PersonaForm

# Create your views here.
def index(request):
	return HttpResponse("Index de Adopción")

def create(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascotas:index')
	else:
		form = PersonaForm()

	return render(request, 'adopcion/create.html', {'form' : form})