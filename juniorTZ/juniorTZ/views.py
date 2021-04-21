from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html',{'User':'shaxzod'})


def team(request):
    return render(request,'team.html',{})