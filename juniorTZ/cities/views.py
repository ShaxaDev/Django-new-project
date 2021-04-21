from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse_lazy
from .models import City
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView, ListView)
from .forms import CityForm


def home(request):
    qs=City.objects.all()
    lst=Paginator(qs,1)
    page_number=request.GET.get('page')
    page_obj=lst.get_page(page_number)
    context={'page_obj':page_obj}
    return render(request,'cities/home.html',context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model=City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Yangi shaxar qo`shildi!'

class CityUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model=City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Shaxar malumotlari o`zgartrildi!'

class CityDeleteView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model=City
    template_name = 'cities/delete_city.html'
    success_url = reverse_lazy('cities:home')
    success_message = 'Shaxar ro`yxatdan o`chirildi!'

class CityListView(ListView):
    model=City
    template_name='cities/home.html'
    paginate_by=3

    def get_context_data(self, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        context['form']=CityForm
        return context

