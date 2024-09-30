from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from Products.models import Product


# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="carts" , null= True , blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)




class CartLine(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name="cartLines")
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="productsLines")
    quantity = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return f"{self.cart} => {self.product} , {self.quantity}"
