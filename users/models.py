from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def cart_items(self):
        return self.items.all()

    def __str__(self):
        return f"Savat - {self.user.username}"
