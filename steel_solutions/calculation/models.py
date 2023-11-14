from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='./media/photos')


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(upload_to='./media/files')


class PogonageUnit(models.Model):
    unit_name = models.CharField(max_length=40)
    metal_thickness = models.IntegerField()
    unit_length = models.IntegerField()
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=1)


class SheetUnit(models.Model):
    unit_name = models.CharField(max_length=40)
    metal_thickness = models.IntegerField()
    unit_width = models.IntegerField()
    unit_height = models.IntegerField()
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=1)


class Sortament(models.Model):
    length_pogon = models.IntegerField()
    width_sheet = models.IntegerField()
    height_sheet = models.IntegerField()
    count = models.IntegerField()


class SortamentType(models.Model):
    sortament = models.ManyToManyField(Sortament)
    unit_pogonage = models.ManyToManyField(PogonageUnit)
    unit_sheet = models.ManyToManyField(SheetUnit)


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
