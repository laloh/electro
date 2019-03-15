from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    price_old = models.FloatField()
    price_new = models.FloatField()

class  Description(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)

class Extra_Info(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    info = models.CharField(max_length=256)

class Review(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    stars = models.IntegerField()

class Comments(models.Model):
    product = models.ForeignKey(Product, 
            on_delete=models.CASCADE)
    stars = models.IntegerField()
    date = models.DateTimeField()
    comment = models.CharField(max_length=256)


