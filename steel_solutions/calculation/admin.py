from django.contrib import admin
from .models import SheetUnit, PogonageUnit, SheetSpec, PogonageSpec, Product, Specification

# Register your models here.
admin.site.register(SheetUnit)
admin.site.register(PogonageUnit)
admin.site.register(SheetSpec)
admin.site.register(PogonageSpec)
admin.site.register(Product)
admin.site.register(Specification)