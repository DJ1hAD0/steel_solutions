from django import forms
from .models import PogonageUnit, SheetUnit


class Pogonage(forms.ModelForm):
    class Meta:
        model = PogonageUnit
        fields = '__all__'


class Sheet(forms.ModelForm):
    class Meta:
        model = SheetUnit
        fields = '__all__'
