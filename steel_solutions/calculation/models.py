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
    unit_name = models.CharField(max_length=40, default='Наименование')
    metal_thickness = models.IntegerField(default=0)
    unit_length = models.IntegerField(default=0)
    unit_weight = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    unit_cost = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    objects = models.Manager()

    def __str__(self):
        return self.unit_name


class SheetUnit(models.Model):
    unit_name = models.CharField(max_length=40, default='Наименование')
    metal_thickness = models.IntegerField(default=0)
    unit_width = models.IntegerField(default=0)
    unit_height = models.IntegerField(default=0)
    unit_weight = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    unit_cost = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    objects = models.Manager()

    def __str__(self):
        return self.unit_name


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    objects = models.Manager()


class SheetSpec(models.Model):
    spec = models.ForeignKey(Specification, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(SheetUnit, on_delete=models.CASCADE)
    width_sheet = models.IntegerField(default=0)
    height_sheet = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    objects = models.Manager()


class PogonageSpec(models.Model):
    spec = models.ForeignKey(Specification, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(PogonageUnit, on_delete=models.CASCADE)
    detail_length = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    objects = models.Manager()
