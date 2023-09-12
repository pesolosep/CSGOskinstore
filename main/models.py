from django.db import models

class Product(models.Model):
    item = models.CharField(max_length=255)
    type = models.TextField()
    price = models.IntegerField()
    amount =  models.IntegerField()
    description = models.TextField()
