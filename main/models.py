from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    skinType =models.TextField(default="-")
    amount = models.IntegerField(default=0)
    description = models.TextField(default="*insert Steam trade link*")