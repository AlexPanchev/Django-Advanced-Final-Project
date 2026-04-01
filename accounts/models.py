from django.conf import settings
from django.db import models
from desserts.models import Ingredient


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    address = models.CharField(
        max_length=255,
        blank=True,
    )
    birthdate = models.DateField(
        blank=True,
        null=True,
    )
    preferred_allergens = models.ManyToManyField(
        Ingredient,
        blank=True,
        related_name="users_avoiding",
    )

    def __str__(self):
        return f"Profile of {self.user.username}"