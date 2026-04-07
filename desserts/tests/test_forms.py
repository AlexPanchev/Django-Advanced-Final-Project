from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from desserts.forms import DessertForm
from desserts.models import Category


class DessertFormTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")

    def test_valid_form(self):
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")

        form = DessertForm(data={
            "name": "Cake",
            "description": "Test",
            "price": 5,
            "category": self.category.pk,
            "is_available": True,
        }, files={"image": image})

        self.assertTrue(form.is_valid())

    def test_invalid_price(self):
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")

        form = DessertForm(data={
            "name": "Cake",
            "description": "Test",
            "price": -1,
            "category": self.category.pk,
        }, files={"image": image})

        self.assertFalse(form.is_valid())