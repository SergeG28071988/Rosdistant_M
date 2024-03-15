from django.shortcuts import render, redirect
from .forms import *
from .models import Man, Woman

# Create your views here.


def index(request):
    context = {
        'title': 'Главная страница сайта'
    }
    return render(request, 'index.html', context)


def man_list(request):
    man = Man.objects.order_by('-id')
    context = {'title': 'Мужчины', 'man': man}
    return render(request, 'man_list.html', context)


def woman_list(request):
    woman = Woman.objects.order_by('-id')
    context = {'title': 'Женщины', 'woman': woman}
    return render(request, 'woman_list.html', context)


def add_man(request):
    error = ''
    if request.method == 'POST':
        form = ManForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма была не верной"
    form = ManForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add_man.html', context)


def add_woman(request):
    error = ''
    if request.method == 'POST':
        form = WomanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма была не верной"
    form = WomanForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add_woman.html', context)
