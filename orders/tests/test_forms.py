from django.test import TestCase
from orders.forms import OrderCreateForm, OrderForm, OrderItemForm
from desserts.models import Category, Dessert


class OrderCreateFormTests(TestCase):
    def test_valid_form(self):
        form = OrderCreateForm(data={
            "customer_name": "John",
            "customer_country_code": "+359",
            "customer_phone_number": "123456789",
            "customer_email": "john@example.com",
            "notes": "",
        })
        self.assertTrue(form.is_valid())

    def test_invalid_phone(self):
        form = OrderCreateForm(data={
            "customer_name": "John",
            "customer_country_code": "+359",
            "customer_phone_number": "123",  # invalid
            "customer_email": "john@example.com",
        })
        self.assertFalse(form.is_valid())


class OrderItemFormTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        self.dessert = Dessert.objects.create(
            name="Cake",
            description="Test",
            price=5,
            category=self.category,
        )

    def test_valid_item_form(self):
        form = OrderItemForm(data={
            "dessert": self.dessert.pk,
            "quantity": 2,
            "unit_price": 5,
        })
        self.assertTrue(form.is_valid())

    def test_invalid_quantity(self):
        form = OrderItemForm(data={
            "dessert": self.dessert.pk,
            "quantity": 0,
            "unit_price": 5,
        })
        self.assertFalse(form.is_valid())