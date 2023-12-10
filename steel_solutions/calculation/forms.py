from django import forms
from .models import PogonageUnit, SheetUnit, SheetSpec, PogonageSpec, Product


class Pogonage(forms.ModelForm):
    class Meta:
        model = PogonageUnit
        fields = '__all__'
        widgets = {'unit_name': forms.TextInput(attrs={'id': 'unit-name', 'class': 'form-control'}),
                   'metal_thickness': forms.NumberInput(attrs={'id': 'metal-thickness', 'class': 'form-control'}),
                   'unit_length': forms.NumberInput(attrs={'id': 'unit-length', 'class': 'form-control'}),
                   'unit_weight': forms.NumberInput(attrs={'id': 'unit-weight', 'class': 'form-control'}),
                   'unit_cost': forms.NumberInput(attrs={'id': 'unit-cost', 'class': 'form-control'})
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
            'unit_weight': 'Вес м2, кг.',
            'unit_cost': 'Стоимость листа, руб.'
        }
        widgets = {'unit_name': forms.TextInput(attrs={'id': 'unit-name', 'class': 'form-control'}),
                   'metal_thickness': forms.NumberInput(attrs={'id': 'metal-thickness', 'class': 'form-control'}),
                   'unit_width': forms.NumberInput(attrs={'id': 'unit-width', 'class': 'form-control'}),
                   'unit_height': forms.NumberInput(attrs={'id': 'unit-height', 'class': 'form-control'}),
                   'unit_weight': forms.NumberInput(attrs={'id': 'unit-weight', 'class': 'form-control'}),
                   'unit_cost': forms.NumberInput(attrs={'id': 'unit-cost', 'class': 'form-control'})
                   }


class SheetSpecForm(forms.ModelForm):
    class Meta:
        model = SheetSpec
        fields = '__all__'
        exclude = ['spec']
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
