from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import Pogonage, Sheet


def index(request):
    return render(request, '<h1>Hello</h1>')


def pogonage_sortament(request):
    if request.method == 'POST':
        form = Pogonage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = Pogonage()
    context = {'form': form}
    return render(request, "calculation/index.html", context)
