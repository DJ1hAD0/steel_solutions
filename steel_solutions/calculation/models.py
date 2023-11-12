from django.db import models



class Product(models.Model):
    id = models.AutoField(primary_key=True)


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='./media/photos')


class File(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.FileField(upload_to='./media/files')


class PogonageUnit(models.Model):
    id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=40)
    metal_thickness = models.IntegerField()
    unit_length = models.IntegerField()
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=1)


class SheetUnit(models.Model):
    id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=40)
    metal_thickness = models.IntegerField()
    unit_width = models.IntegerField()
    unit_height = models.IntegerField()
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=1)


class Sortament(models.Model):
    id = models.AutoField(primary_key=True)
    length_pogon = models.IntegerField()
    width_sheet = models.IntegerField()
    height_sheet = models.IntegerField()
    count = models.IntegerField()


class SortamentType(models.Model):
    id = models.AutoField(primary_key=True)
    sortament_id = models.ManyToManyField(Sortament)
    unit_pogonage_id = models.ManyToManyField(PogonageUnit)
    unit_sheet_id = models.ManyToManyField(SheetUnit)


class Specification(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
