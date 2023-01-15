from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(name='phoneModel')


