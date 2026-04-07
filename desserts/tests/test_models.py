from django.test import TestCase
from desserts.models import Category, Ingredient, Dessert
from django.core.exceptions import ValidationError

class CategoryModelTests(TestCase):
    def test_category_str(self):
        category = Category.objects.create(name="Cakes")
        self.assertEqual(str(category), "Cakes")

    def test_category_unique_name(self):
        Category.objects.create(name="Cakes")
        with self.assertRaises(Exception):
            Category.objects.create(name="Cakes")


class IngredientModelTests(TestCase):
    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Sugar")
        self.assertEqual(str(ingredient), "Sugar")

    def test_allergen_flag_default(self):
        ingredient = Ingredient.objects.create(name="Milk")
        self.assertFalse(ingredient.is_allergen)


class DessertModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        self.ingredient = Ingredient.objects.create(name="Flour")

    def test_dessert_str(self):
        dessert = Dessert.objects.create(
            name="Chocolate Cake",
            description="Rich chocolate cake",
            price=5.50,
            category=self.category,
        )
        self.assertEqual(str(dessert), "Chocolate Cake")

    def test_price_must_be_positive(self):
        dessert = Dessert(
            name="Bad Cake",
            description="Invalid",
            price=-1,
            category=self.category,
        )
        with self.assertRaises(ValidationError):
            dessert.full_clean()

    def test_ingredients_many_to_many(self):
        dessert = Dessert.objects.create(
            name="Cake",
            description="Test",
            price=3.00,
            category=self.category,
        )
        dessert.ingredients.add(self.ingredient)
        self.assertEqual(dessert.ingredients.count(), 1)