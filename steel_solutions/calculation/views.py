from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from pyexpat.errors import messages
from django.db import models
from .forms import Pogonage, Sheet, SheetSpecForm, PogonSpecForm
from .models import Specification, Product, SheetSpec, PogonageSpec, SheetUnit, PogonageUnit


def index(request):
    return render(request, '<h1>Hello</h1>')


def show_unit_sortament(model, form, type):
    unit_types = model.objects.all()
    result = []
    for unit_type in unit_types:
        form_data = form(initial=unit_type.__dict__)
        result.append({'id': unit_type.id, 'form': form_data, 'type': type})
    context = {'forms': result}
    return context


def pogonage_sortament(request):
    context = show_unit_sortament(model=PogonageUnit, form=Pogonage, type='pogon')
    return render(request, "calculation/pogonage.html", context)


def sheet_sortament(request):
    context = show_unit_sortament(model=SheetUnit, form=Sheet, type='sheet')
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


def crud_unit_mapper(unit_type):
    models_mapping = {'pogon': PogonageUnit,
                      'sheet': SheetUnit}
    forms_mapping = {'pogon': Pogonage,
                     'sheet': Sheet}
    return models_mapping.get(unit_type), forms_mapping.get(unit_type)


def crud_spec_mapper(spec_type):
    models_mapping = {'pogon': PogonageSpec,
                      'sheet': SheetSpec}
    forms_mapping = {'pogon': PogonSpecForm,
                     'sheet': SheetSpecForm}
    return models_mapping.get(spec_type), forms_mapping.get(spec_type)


def delete_spec_entry(request):
    if request.method == "POST":
        model, _ = crud_spec_mapper(spec_type=request.POST.get('item_type'))
        model.objects.get(id=request.POST['item_id']).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def create_spec_entry(request):
    if request.method == "POST":
        metal_type = request.POST.get('item_type')
        unit_model, _ = crud_unit_mapper(unit_type=metal_type)
        model, _ = crud_spec_mapper(spec_type=metal_type)
        model.objects.create(spec=Specification.objects.get(id=request.POST['spec']),
                             unit_type=unit_model.objects.first())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def update_spec_entry(request):
    if request.method == "POST":
        metal_type = request.POST.get('type')
        unit_model, _ = crud_unit_mapper(unit_type=metal_type)
        model, form = crud_spec_mapper(spec_type=metal_type)
        spec_instance = get_object_or_404(model, pk=request.POST.get('id'))
        form_data = form(request.POST, instance=spec_instance)
        if form_data.is_valid():
            form_data.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def create_unit_entry(request):
    if request.method == "POST":
        model, _ = crud_unit_mapper(unit_type=request.POST.get('item_type'))
        model.objects.create()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def update_unit_entry(request):
    if request.method == "POST":
        model, form = crud_unit_mapper(unit_type=request.POST.get('type'))
        unit_instance = get_object_or_404(model, pk=request.POST.get('id'))
        form_data = form(request.POST, instance=unit_instance)
        if form_data.is_valid():
            form_data.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))


def delete_unit_entry(request):
    if request.method == "POST":
        model, _ = crud_unit_mapper(unit_type=request.POST.get('item_type'))
        model.objects.get(id=request.POST['item_id']).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '<default_url>'))
