from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from pyexpat.errors import messages
from django.db import models
from .forms import Pogonage, Sheet, SheetSpecForm, PogonSpecForm
from .models import Specification, Product, SheetSpec, PogonageSpec, SheetUnit, PogonageUnit


def index(request):
    return render(request, '<h1>Hello</h1>')


def pogonage_sortament(request):
    if request.method == 'POST':
        form = Pogonage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pogonage')
    form = Pogonage()
    context = {'form': form}
    return render(request, "calculation/pogonage.html", context)


def sheet_sortament(request):
    if request.method == 'POST':
        form = Sheet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sheet')
    form = Sheet()
    context = {'form': form}
    return render(request, "calculation/sheet.html", context)


def save_sheet_entry(request):
    form = SheetSpecForm(request.POST)
    if form.is_valid():
        instance = SheetSpec.objects.get(id=request.POST.get('id'))
        instance.unit_type = SheetUnit.objects.get(id=request.POST['unit_type'])
        instance.width_sheet = request.POST['width_sheet']
        instance.height_sheet = request.POST['height_sheet']
        instance.amount = request.POST['amount']
        instance.save()


def save_pogon_entry(request):
    form = PogonSpecForm(request.POST)
    if form.is_valid():
        instance = PogonageSpec.objects.get(id=request.POST.get('id'))
        instance.unit_type = PogonageUnit.objects.get(id=request.POST['unit_type'])
        instance.detail_length = request.POST['detail_length']
        instance.amount = request.POST['amount']
        instance.save()


def spec(request, product_id):
    if request.method == "POST":
        if request.POST.get('type') == 'sheet':
            save_sheet_entry(request)
        elif request.POST.get('type') == 'pogon':
            save_pogon_entry(request)
    spec_id = Specification.objects.get(pk=product_id).id
    sheet_spec = SheetSpec.objects.filter(spec_id=spec_id)
    pogonage_spec = PogonageSpec.objects.filter(spec_id=spec_id)
    result_sheet = []
    result_pogon = []
    for item_sheet in sheet_spec:
        form_sheet_metall = SheetSpecForm(initial={
            'unit_type': SheetUnit.objects.get(id=item_sheet.unit_type_id).pk,
            'width_sheet': item_sheet.width_sheet,
            'height_sheet': item_sheet.height_sheet,
            'amount': item_sheet.amount})
        result_sheet.append({'id': item_sheet.id, 'form': form_sheet_metall, 'type': 'sheet', 'spec_id': spec_id})
    for item_pogon in pogonage_spec:
        form_pogon_metall = PogonSpecForm(initial={
            'unit_type': PogonageUnit.objects.get(id=item_pogon.unit_type_id).pk,
            'detail_length': item_pogon.detail_length,
            'amount': item_pogon.amount})
        result_pogon.append({'id': item_pogon.id, 'form': form_pogon_metall, 'type': 'pogon', 'spec_id': spec_id})
    return render(request, "calculation/spec.html", context={'spec_sheet': result_sheet, 'spec_pogon': result_pogon})


def delete_spec_entry(request):
    if request.method == "POST":
        if request.POST['item_type'] == 'sheet':
            SheetSpec.objects.get(id=request.POST['item_id']).delete()
        elif request.POST['item_type'] == 'pogon':
            PogonageSpec.objects.get(id=request.POST['item_id']).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def create_spec_entry(request):
    if request.method == "POST":
        spec = Specification.objects.get(id=request.POST['spec'])
        if request.POST['item_type'] == 'sheet':
            SheetSpec.objects.create(spec=spec, unit_type=SheetUnit.objects.first(), width=0, height=0,
                                     amount=0)
        elif request.POST['item_type'] == 'pogon':
            PogonageSpec.objects.create(spec=spec, unit_type=PogonageUnit.objects.first(), detail_length=0,
                                        amount=0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))
