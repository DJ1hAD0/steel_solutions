from django import forms
from .models import PogonageUnit, SheetUnit, SheetSpec, PogonageSpec, Product


class Pogonage(forms.ModelForm):
    class Meta:
        model = PogonageUnit
        fields = '__all__'
        labels = {
            'unit_name': 'Наименование',
            'metal_thickness': 'Толщина стенки, мм.',
            'unit_length': 'Длина хлыста, мм.',
            'unit_weight': 'Вес одного хлыста, кг.',
            'unit_cost': 'Стоимость одной единицы, руб.',
        }


class Sheet(forms.ModelForm):
    class Meta:
        model = SheetUnit
        fields = '__all__'
        labels = {
            'unit_name': 'Наименование',
            'metal_thickness': 'Толщина листа, мм.',
            'unit_width': 'Ширина листа, мм.',
            'unit_height': 'Длина листа, мм.',
            'unit_weight': 'Вес листа, кг.',
            'unit_cost': 'Стоимость листа, руб.'
        }


class SheetSpecForm(forms.ModelForm):
    class Meta:
        model = SheetSpec
        fields = '__all__'
        exclude = ['spec']
        labels = {'unit_type': 'Тип',
                  'width_sheet': 'Ширина',
                  'height_sheet': 'Высота',
                  'amount': 'Кол-во'}
        widgets = {'unit_type': forms.Select(attrs={'id': 'unit-type', 'class': 'form-select'}),
                   'width_sheet': forms.TextInput(attrs={'id': 'width-sheet', 'class': 'form-control'}),
                   'height_sheet': forms.TextInput(attrs={'id': 'height-sheet', 'class': 'form-control'}),
                   'amount': forms.TextInput(attrs={'id': 'amount', 'class': 'form-control'}),
                   }


class PogonSpecForm(forms.ModelForm):
    class Meta:
        model = PogonageSpec
        fields = '__all__'
        exclude = ['spec']
        labels = {'unit_type': 'Тип',
                  'detail_length': 'Длина',
                  'amount': 'Кол-во'}
        widgets = {'unit_type': forms.Select(attrs={'id': 'unit-type', 'class': 'form-select'}),
                   'detail_length': forms.TextInput(attrs={'id': 'detail-length', 'class': 'form-control'}),
                   'amount': forms.TextInput(attrs={'id': 'amount', 'class': 'form-control'}),
                   }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {'name': 'Наименование',
                  'description': 'Описание',
                  'price': 'Цена'}
        widgets = {'name': forms.TextInput(attrs={'id': 'product-name', 'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'id': 'product-description', 'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'id': 'product-price', 'class': 'form-control'}),
                   }
