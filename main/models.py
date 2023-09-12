from django.db import models

class Product(models.Model):
    item = models.TextField()
    type = models.TextField()
    price = models.IntegerField()
    amount =  models.IntegerField()
    description = models.TextField()
