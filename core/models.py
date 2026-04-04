from django.db import models
from django.conf import settings
from desserts.models import Dessert

# Create your models here.

class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.line_total() for item in self.items.all())

    def __str__(self):
        return f"Basket for {self.user.username}"

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="items")
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def line_total(self):
        return self.dessert.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.dessert.name} in basket of {self.basket.user.username}"
