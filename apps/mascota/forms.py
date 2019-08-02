from django import forms
from apps.mascota.models import Mascota

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
			'fecha_rescate' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'persona' : forms.Select(attrs = {'class' : 'form-control'}),
			'vacuna' : forms.CheckboxSelectMultiple(),
		}