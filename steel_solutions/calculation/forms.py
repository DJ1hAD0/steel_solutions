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


class PogonSpecForm(forms.ModelForm):
    class Meta:
        model = PogonageSpec
        fields = '__all__'
        exclude = ['spec']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {'image': 'Изображение',
                  'name': 'Наименование',
                  'description': 'Описание',
                  'price': 'Цена'}
        widgets = {'name': forms.TextInput(attrs={'id': 'product-name', 'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'id': 'product-description', 'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'id': 'product-price', 'class': 'form-control'}),
                   }

# id = models.AutoField(primary_key=True)
#    image = models.ImageField(upload_to='products/', default=None)
#    name = models.CharField(max_length=40, default='test')
#    description = models.CharField(max_length=500, default='tst')
#    price = models.IntegerField(default=0)
#    objects = models.Manager()
