from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Category Name",
        help_text="Enter the name of the dessert category (e.g. Cakes, Cookies).",
        error_messages={
            "unique": "This category already exists.",
            "max_length": "Category name cannot exceed 50 characters.",
        }
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Optional: short description of this category."
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name



class Ingredient(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Ingredient Name",
        help_text="Enter the ingredient name.",
    )
    is_allergen = models.BooleanField(
        default=False,
        verbose_name="Contains Allergen",
        help_text="Mark if this ingredient is a known allergen."
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Dessert Name",
        help_text="Enter the name of the dessert.",
        error_messages={
            "max_length": "Dessert name cannot exceed 100 characters.",
            "unique": "A dessert with this name already exists."
        }
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Describe the dessert in detail."
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Price",
        help_text="Enter the price in EUR.",
        error_messages={
            "min_value": "Price must be greater than zero."
        }
    )
    image = models.ImageField(
        upload_to="desserts/",
        verbose_name="Image",
        help_text="Upload an image of the dessert.",
        error_messages={
            "required": "An image is required for this dessert.",
            "invalid": "Please upload a valid image file."
        }
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Available",
        help_text="Uncheck if this dessert is currently unavailable."
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="desserts",
        verbose_name="Category",
        help_text="Select the category for this dessert."
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="desserts",
        blank=True,
        verbose_name="Ingredients",
        help_text="Select the ingredients used in this dessert."
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name