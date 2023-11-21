from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import Pogonage, Sheet
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


def spec(request, product_id):
    spec_id = Specification.objects.get(pk=product_id).id
    sheet_spec = SheetSpec.objects.filter(spec_id=spec_id)
    pogonage_spec = PogonageSpec.objects.filter(spec_id=spec_id)
    result_lst = []
    for item_sheet in sheet_spec:
        result = {}
        result['unit_name'] = SheetUnit.objects.get(id=item_sheet.unit_type_id).unit_name
        result['width'] = item_sheet.width_sheet
        result['height'] = item_sheet.height_sheet
        result['amount'] = item_sheet.amount
        result_lst.append(result)
    for item_pogon in pogonage_spec:
        result = {}
        result['unit_name'] = PogonageUnit.objects.get(id=item_pogon.unit_type_id).unit_name
        result['length'] = item_pogon.detail_length
        result['amount'] = item_pogon.amount
        result_lst.append(result)
    return render(request, "calculation/spec.html", context={'spec': result_lst})
