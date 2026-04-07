from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from desserts.models import Category, Dessert

class DessertPermissionTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        self.dessert = Dessert.objects.create(
            name="Cake",
            description="Test",
            price=5,
            category=self.category,
        )
        self.user = User.objects.create_user(username="u", password="1234")

    def test_create_requires_permission(self):
        self.client.login(username="u", password="1234")
        response = self.client.get(reverse("dessert_create"))
        self.assertEqual(response.status_code, 403)

    def test_create_allowed_with_permission(self):
        perm = Permission.objects.get(codename="add_dessert")
        self.user.user_permissions.add(perm)
        self.client.login(username="u", password="1234")
        response = self.client.get(reverse("dessert_create"))
        self.assertEqual(response.status_code, 200)