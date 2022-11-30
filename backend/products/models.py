from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(blank=True,null=True,max_length=120)
    price=models.DecimalField(max_digits=15,decimal_places=2)
    def __str__(self):
        return (f"{self.title}")
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def discount(self):
        return "122"

