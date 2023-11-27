import decimal

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from pyexpat.errors import messages
from django.db import models
from .forms import Pogonage, Sheet, SheetSpecForm, PogonSpecForm, ProductForm
from .models import Specification, Product, SheetSpec, PogonageSpec, SheetUnit, PogonageUnit


def index(request):
    return render(request, "calculation/index.html")


def get_spec(product_id):
    spec_id = Specification.objects.get(product_id=product_id).id
    sheet_spec = SheetSpec.objects.filter(spec_id=spec_id)
    pogonage_spec = PogonageSpec.objects.filter(spec_id=spec_id)
    result_sheet = []
    result_pogon = []
    summary_weight = 0
    summary_cost = 0
    for item_sheet in sheet_spec:
        sheet_unit_type = SheetUnit.objects.get(id=item_sheet.unit_type_id)
        calc_sheet = calculate_sheet_spec_entry(sheet_unit_type, item_sheet.width_sheet, item_sheet.height_sheet,
                                                item_sheet.amount)
        summary_weight += calc_sheet['weight']
        summary_cost += calc_sheet['cost']
        form_sheet_metall = SheetSpecForm(initial={
            'unit_type': sheet_unit_type.pk,
            'width_sheet': item_sheet.width_sheet,
            'height_sheet': item_sheet.height_sheet,
            'amount': item_sheet.amount})
        result_sheet.append({'id': item_sheet.id, 'form': form_sheet_metall, 'type': 'sheet', 'calc': calc_sheet})
    for item_pogon in pogonage_spec:
        pogon_unit_type = PogonageUnit.objects.get(id=item_pogon.unit_type_id)
        calc_pogon = calculate_pogon_spec_entry(pogon_unit_type, item_pogon.detail_length, item_pogon.amount)
        summary_weight += calc_pogon['weight']
        summary_cost += calc_pogon['cost']
        form_pogon_metall = PogonSpecForm(initial={
            'unit_type': pogon_unit_type.pk,
            'detail_length': item_pogon.detail_length,
            'amount': item_pogon.amount})
        result_pogon.append({'id': item_pogon.id, 'form': form_pogon_metall, 'type': 'pogon', 'calc': calc_pogon})
    return {'spec_sheet': result_sheet, 'spec_pogon': result_pogon, 'spec_id': spec_id, 'sum_weight': summary_weight,
            'sum_cost': summary_cost}


def calculate_sheet_spec_entry(unit_type, width_detail, height_detail, amount):
    unit_num = round(
        decimal.Decimal((width_detail * height_detail) / (unit_type.unit_width * unit_type.unit_height)) * amount, 4)
    weight = round(
        decimal.Decimal((width_detail / 1000 * height_detail / 1000)) * amount * unit_type.unit_weight, 1)
    cost = round(unit_num * unit_type.unit_cost)
    return {'num': unit_num, 'weight': weight, 'cost': cost}


def calculate_pogon_spec_entry(unit_type, length_detail, amount):
    unit_num = round(decimal.Decimal(length_detail / unit_type.unit_length) * amount, 4)
    weight = round(decimal.Decimal(length_detail / 1000) * amount * unit_type.unit_weight, 1)
    cost = round(unit_num * unit_type.unit_cost)
    return {'num': unit_num, 'weight': weight, 'cost': cost}


def product(request, product_id):
    obj = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            redirect('product', product_id)
    form = ProductForm(initial=obj.__dict__)
    img = obj.image
    product_description = {'id': obj.id, 'form_product': form, 'img_product': img}
    product_spec = get_spec(product_id)
    return render(request, "calculation/product.html", context={**product_description, **product_spec})


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


def list_products(request):
    products = Product.objects.all()
    to_template = [product for product in products]
    return render(request, "calculation/products.html", context={'product_list': to_template})


def create_product(request):
    product_id = Product.objects.create().id
    Specification.objects.create(product_id=product_id)
    return redirect('product', product_id)


def delete_product(request, product_id):
    Product.objects.get(pk=product_id).delete()
    return redirect('list_products')
