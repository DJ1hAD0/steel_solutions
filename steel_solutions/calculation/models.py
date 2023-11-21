from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500, default='tst')
    price = models.IntegerField(default=0)


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
    objects = models.Manager()


class SheetUnit(models.Model):
    unit_name = models.CharField(max_length=40)
    metal_thickness = models.IntegerField()
    unit_width = models.IntegerField()
    unit_height = models.IntegerField()
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=1)
    objects = models.Manager()


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    objects = models.Manager()


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
