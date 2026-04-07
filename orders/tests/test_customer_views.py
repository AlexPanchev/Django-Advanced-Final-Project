from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from desserts.models import Category, Dessert
from orders.models import Order


class MyOrdersViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alex", password="1234")
        self.other = User.objects.create_user(username="john", password="1234")

        self.order1 = Order.objects.create(
            customer_name="Alex",
            customer_phone="+359 123456789",
            customer_email="alex@example.com",
            user=self.user,
        )
        self.order2 = Order.objects.create(
            customer_name="John",
            customer_phone="+359 123456789",
            customer_email="john@example.com",
            user=self.other,
        )




class CustomerOrderDetailTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alex", password="1234")
        self.order = Order.objects.create(
            customer_name="Alex",
            customer_phone="+359 123456789",
            customer_email="alex@example.com",
            user=self.user,
        )

    def test_user_can_view_own_order(self):
        self.client.login(username="alex", password="1234")
        response = self.client.get(reverse("customer_order_detail", args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_view_others_order(self):
        other = User.objects.create_user(username="john", password="1234")
        self.client.login(username="john", password="1234")
        response = self.client.get(reverse("customer_order_detail", args=[self.order.pk]))
        self.assertEqual(response.status_code, 404)