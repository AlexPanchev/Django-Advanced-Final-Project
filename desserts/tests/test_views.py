from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from desserts.models import Dessert, Category

class DessertListViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        Dessert.objects.create(
            name="Cake 1",
            description="Test",
            price=5,
            category=self.category,
            is_available=True,
        )
        Dessert.objects.create(
            name="Cake 2",
            description="Test",
            price=5,
            category=self.category,
            is_available=False,
        )

    def test_list_shows_only_available(self):
        response = self.client.get(reverse("dessert_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cake 1")
        self.assertNotContains(response, "Cake 2")

    def test_search_filters_results(self):
        response = self.client.get(reverse("dessert_list"), {"q": "Cake 1"})
        self.assertContains(response, "Cake 1")
        self.assertNotContains(response, "Cake 2")


class DessertDetailViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        self.dessert = Dessert.objects.create(
            name="Cake",
            description="Test",
            price=5,
            category=self.category,
        )

    def test_detail_view_loads(self):
        response = self.client.get(reverse("dessert_detail", args=[self.dessert.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cake")


class AllDessertsListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="staff", password="1234")
        perm = Permission.objects.get(codename="view_dessert")
        self.user.user_permissions.add(perm)

    def test_requires_login(self):
        response = self.client.get(reverse("all_desserts_list"))
        self.assertEqual(response.status_code, 302)

    def test_requires_permission(self):
        self.client.login(username="staff", password="1234")
        response = self.client.get(reverse("all_desserts_list"))
        self.assertEqual(response.status_code, 200)