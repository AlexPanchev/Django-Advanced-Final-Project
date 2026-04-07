from django.test import TestCase
from django.contrib.auth.models import User
from desserts.models import Category, Dessert
from orders.models import Order, OrderItem


class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alex", password="1234")
        self.category = Category.objects.create(name="Cakes")
        self.dessert = Dessert.objects.create(
            name="Chocolate Cake",
            description="Test",
            price=5,
            category=self.category,
        )
        self.order = Order.objects.create(
            customer_name="John Doe",
            customer_phone="+359 123456789",
            customer_email="john@example.com",
            user=self.user,
        )

    def test_order_str(self):
        self.assertIn("John Doe", str(self.order))

    def test_total_price(self):
        OrderItem.objects.create(
            order=self.order,
            dessert=self.dessert,
            quantity=2,
            unit_price=5,
        )
        self.assertEqual(self.order.total_price(), 10)


class OrderItemModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        self.dessert = Dessert.objects.create(
            name="Cake",
            description="Test",
            price=5,
            category=self.category,
        )
        self.order = Order.objects.create(
            customer_name="John",
            customer_phone="+359 123456789",
            customer_email="john@example.com",
        )

    def test_line_total(self):
        item = OrderItem.objects.create(
            order=self.order,
            dessert=self.dessert,
            quantity=3,
            unit_price=4,
        )
        self.assertEqual(item.line_total(), 12)