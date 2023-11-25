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
    unit_types = PogonageUnit.objects.all()
    result = []
    for unit_type in unit_types:
        form = Pogonage(initial=unit_type.__dict__)
        result.append({'id': unit_type.id, 'form': form})
    context = {'forms': result}
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


def spec(request, product_id):
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
        result_sheet.append({'id': item_sheet.id, 'form': form_sheet_metall, 'type': 'sheet'})
    for item_pogon in pogonage_spec:
        form_pogon_metall = PogonSpecForm(initial={
            'unit_type': PogonageUnit.objects.get(id=item_pogon.unit_type_id).pk,
            'detail_length': item_pogon.detail_length,
            'amount': item_pogon.amount})
        result_pogon.append({'id': item_pogon.id, 'form': form_pogon_metall, 'type': 'pogon'})
    return render(request, "calculation/spec.html",
                  context={'spec_sheet': result_sheet, 'spec_pogon': result_pogon, 'spec_id': spec_id})


def delete_spec_entry(request):
    if request.method == "POST":
        if request.POST['item_type'] == 'sheet':
            SheetSpec.objects.get(id=request.POST['item_id']).delete()
        elif request.POST['item_type'] == 'pogon':
            PogonageSpec.objects.get(id=request.POST['item_id']).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def create_spec_entry(request):
    if request.method == "POST":
        current_spec = Specification.objects.get(id=request.POST['spec'])
        if request.POST['item_type'] == 'sheet':
            SheetSpec.objects.create(spec=current_spec, unit_type=SheetUnit.objects.first(), width_sheet=0,
                                     height_sheet=0,
                                     amount=0)
        elif request.POST['item_type'] == 'pogon':
            PogonageSpec.objects.create(spec=current_spec, unit_type=PogonageUnit.objects.first(), detail_length=0,
                                        amount=0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def update_spec_entry(request):
    if request.method == "POST":
        if request.POST.get('type') == 'sheet':
            sheet_spec_instance = get_object_or_404(SheetSpec, pk=request.POST.get('id'))
            form = SheetSpecForm(request.POST, instance=sheet_spec_instance)
            if form.is_valid():
                form.save()
        elif request.POST.get('type') == 'pogon':
            pogon_spec_instance = get_object_or_404(PogonageSpec, pk=request.POST.get('id'))
            form = PogonSpecForm(request.POST, instance=pogon_spec_instance)
            if form.is_valid():
                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def update_pogonage_unit_entry(request):
    if request.method == "POST":
        pogonage_unit_instance = get_object_or_404(PogonageUnit, pk=request.POST.get('id'))
        form = Pogonage(request.POST, instance=pogonage_unit_instance)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def delete_pogonage_unit_entry(request):
    if request.method == "POST":
        PogonageUnit.objects.get(id=request.POST['item_id']).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def create_pogonage_unit_entry(request):
    if request.method == "POST":
        PogonageUnit.objects.create(unit_name='Наименование', metal_thickness=1, unit_length=6000, unit_weight=0,
                                    unit_cost=0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))
