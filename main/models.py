from django.db import models

# Create your models here.
from django.db import models

class Pesanan(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    skinType =models.TextField(default="-")
    amount = models.IntegerField(default=0)
    tradeLink = models.TextField(default="-")

