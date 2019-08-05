from django import forms
from apps.mascota.models import Mascota, Vacuna

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota
		fields = [
			'nombre',
			'tipo',
			'edad',
			'fecha_rescate',
			'persona',
			'vacuna',
		]
		label = {
			'nombre' : 'Nombre',
			'tipo' : 'Tipo',
			'edad' : 'Edad',
			'fecha_rescate' : 'Fecha de rescate',
			'persona' : 'Rescatador',
			'vacuna' : 'Vacuna',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'tipo' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'edad' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'fecha_rescate' : forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'date'}),
			'persona' : forms.Select(attrs = {'class' : 'form-control'}),
			'vacuna' : forms.CheckboxSelectMultiple(),
		}

class VacunaForm(forms.ModelForm):
	
	class Meta:
		model = Vacuna
		fields = [
			'nombre',
			'caducidad',
		]
		label = {
			'nombre' : 'Nombre',
			'caducidad' : 'Fecha de caducidad',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'caducidad' : forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'date'}),
		}
