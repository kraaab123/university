from django.shortcuts import render, redirect
from avto import forms
from avto import models

def home(request):
    context = {}
    context['hello'] = 'hello'
    return render (request,'home.html', context)


def engine(request):
    context = {}
    context['object'] = ['str', 1231, 'TT']
    return render(request, 'engine.html', context)


def base(reguest):
    return render (reguest, 'base.html', )


def Hararteristiki(request):
    context = {
        'Engine': models.Manufacturer.objects.all()
    }
    return render(request, 'home.html', context)


def Hararteristiki1(request):
    context = {
        'Engine': models.Engine.objects.all(),
        'Man': models.Manufacturer.objects.all()
    }
    return render(request, 'home.html', context)