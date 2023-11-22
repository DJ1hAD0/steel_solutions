from django import forms
from .models import PogonageUnit, SheetUnit, SheetSpec, PogonageSpec


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


"""
class SheetSpec(models.Model):
    spec = models.ForeignKey(Specification, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(SheetUnit, on_delete=models.CASCADE)
    width_sheet = models.IntegerField()
    height_sheet = models.IntegerField()
    amount = models.IntegerField()
    objects = models.Manager()


class PogonageSpec(models.Model):
    spec = models.ForeignKey(Specification, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(PogonageUnit, on_delete=models.CASCADE)
    detail_length = models.IntegerField()
    amount = models.IntegerField()
    objects = models.Manager()
"""


class SheetSpecForm(forms.ModelForm):
    class Meta:
        model = SheetSpec
        fields = '__all__'
        exclude = ['spec']


class PogonSpecForm(forms.ModelForm):
    class Meta:
        model = PogonageSpec
        fields = '__all__'
        exclude = ['spec']
