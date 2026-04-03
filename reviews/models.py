from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from desserts.models import Dessert


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    dessert = models.ForeignKey(
        Dessert,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "dessert")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} → {self.dessert.name} ({self.rating}/5)"
