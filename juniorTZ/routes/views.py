from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from .forms import RouteForm, RouteModelForm
from .models import Route
from .utils import get_routes
from cities.models import City
from trains.models import Train


def home(request):
    form=RouteForm()
    return render(request,'routes/home.html',{'form':form})


def find_routes(request):
    if request.method=='POST':
        form=RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request,e)
                return render(request, 'routes/home.html', {'form': form})
            messages.success(request,'Marxamat natijalarni ko`rishingz mumkin')
            return render(request, 'routes/home.html',context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form=RouteForm()
        return render(request, 'routes/home.html', {'form': form})

def result(request,**kwargs):
    response=kwargs['context']
    lst = Paginator(response['routes'], 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    return render(request,'routes/result.html',{'page_obj':page_obj})


def add_routes(request):
    if request.method=='POST':
        context={}
        data=request.POST
        if data:
            from_city_id=int(data['from_city'])
            to_city_id=int(data['to_city'])
            total_time=int(data['total_time'])
            trains=data['trains'].split(',')
            trains_lst=[int(t) for t in trains if t.isdigit() ]
            qs=Train.objects.filter(id__in=trains_lst).select_related('from_city','to_city')
            cities=City.objects.filter(id__in=[from_city_id,to_city_id]).in_bulk()
            form=RouteModelForm(
                initial={
                    'from_city':cities[from_city_id],
                    'to_city':cities[to_city_id],
                    'trains':qs,
                    'travel_times':total_time,
                }
            )
            context['form']=form
        return render(request,'routes/create.html',context)
    else:
        messages.error(request,'Yo`l saqlashda xatolik')
        return redirect('/')

def save_route(request):
    if request.method=='POST':
        form=RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Ajoyib yo`l saqlandi!')
            return redirect('/')
        return render(request,'routes/create.html',{'form':form})
    else:
        messages.error(request,'Saqlashda xatolik aniqlandi !')
        return redirect('/')

class RouteListView(ListView):
    paginate_by = 10
    model=Route
    template_name = 'routes/list.html'

class RouteDetailView(DetailView):
    queryset=Route.objects.all()
    template_name = 'routes/detail.html'

class RouteDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model=Route
    success_url = reverse_lazy('home')
    redirect_field_name = 'login'
    success_message = 'Yo`l ro`yxatdan o`chirildi'

    def post(self, request, *args, **kwargs):
        messages.success(request,'Yo`l o`chirildi!')
        return super().post(request, *args, **kwargs)
