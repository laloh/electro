from django.db import models

"""
TODO:
[x] Investigar como enviar los Modelos a PostgreSQL nueva versión.
[x] Hacer Pruebas de Inserción.
[x] Agregar URL para la Imagen
[ ] Utilizar Fake data para popular información
[ ] Los Productos más vendidos serán los ultimos 10 Ids Insertados
[ ] Los más vendidos tienen que ser seleccionados manualmente
[ ] Actualizar los precios utilizando el código de Amazon (Todos los días)
[ ] Si el precio viejo no existe, que Django se encargue de rebajarlo
[ ] Programar una Barra de progreso

FIXME:

"""

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    price_old = models.FloatField()
    price_new = models.FloatField()

    def __str__(self):
        return self.name

class Description(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.product.__str__()

class Extra_Info(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    info = models.CharField(max_length=256)
    
    def __str__(self):
        return self.product.__str__()

class Review(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    stars = models.IntegerField()
    
    def __str__(self):
        return self.product.__str__()

class Comments(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    stars = models.IntegerField()
    date = models.DateTimeField()
    comment = models.CharField(max_length=256)

    def __str__(self):
        return self.product.__str__()

class Images(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    url = models.CharField(max_length=256)

    def __str__(self):
        return self.product.__str__()



