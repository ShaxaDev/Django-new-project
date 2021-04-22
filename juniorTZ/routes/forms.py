from django import forms

from cities.models import City
from django.contrib.auth.models import User
from routes.models import Route
from trains.models import Train
from django.utils.safestring import mark_safe

class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label=mark_safe('<b>Qaysi shahardan</b>'),
                                     empty_label='shahar tanlang',
                                     queryset=City.objects.all(),
                                     widget=forms.Select(
                                     attrs={'class':'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label=mark_safe('<b>Qaysi shaharga</b>'),
                                     empty_label='shahar tanlang',
                                     queryset=City.objects.all(),
                                     widget=forms.Select(
                                     attrs={'class': 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label=mark_safe('<b>Qaysi shahar orqali</b>'),
                                     queryset=City.objects.all(),required=False,
                                     widget=forms.SelectMultiple(
                                     attrs={'class': 'form-control js-example-basic-multiple'}))
    travelling_time = forms.DateField(label=mark_safe('<b>Ketish kuni</b>'),
                                     widget=forms.DateInput(
                                     attrs={'class': 'form-control', 'type':'date','placeholder': 'Qachon?', 'type': 'text',
                                     'onfocus': "(this.type='date')",}))




class RouteModelForm(forms.ModelForm):
    name=forms.CharField(label='Yo`l nomi',
                                    widget=forms.TextInput(
                                    attrs={'class':'from-control','placeholder':'misol: TR123'}))
    from_city = forms.ModelChoiceField(
                                     queryset=City.objects.all(),
                                     widget=forms.HiddenInput())
    to_city = forms.ModelChoiceField(
                                     queryset=City.objects.all(),
                                     widget=forms.HiddenInput())
    trains = forms.ModelMultipleChoiceField(label='through city',
                                     queryset=Train.objects.all(),required=False,
                                     widget=forms.SelectMultiple(
                                     attrs={'class': 'form-control d-none'}))
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    ticket_number=forms.IntegerField(widget=forms.HiddenInput())

    passenger=forms.ModelChoiceField(queryset=User.objects.all(),
                                     widget=forms.HiddenInput())


    class Meta:
        model=Route
        fields='__all__'