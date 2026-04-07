from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from desserts.models import Category, Dessert
from orders.models import Order, OrderItem


class OrderListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="staff", password="1234")
        perm = Permission.objects.get(codename="view_order")
        self.user.user_permissions.add(perm)

    def test_requires_login(self):
        response = self.client.get(reverse("order_list"))
        self.assertEqual(response.status_code, 302)

    def test_requires_permission(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(reverse("order_list"))
        self.assertEqual(response.status_code, 200)


class OrderDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="staff", password="1234")
        perm = Permission.objects.get(codename="view_order")
        self.user.user_permissions.add(perm)

        self.order = Order.objects.create(
            customer_name="John",
            customer_phone="+359 123456789",
            customer_email="john@example.com",
        )

    def test_detail_view(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(reverse("order_detail", args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")