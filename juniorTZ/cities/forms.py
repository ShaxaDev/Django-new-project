from django import forms

from .models import City


class CityForm(forms.ModelForm):
    name=forms.CharField(label='Shaxar',
                         widget=forms.TextInput(
                         attrs={'class':'form-control','placeholder':'misol: Buxoro'}))

    class Meta:
        model=City
        fields=('name','shahar_haqida_qisqa','about_city')