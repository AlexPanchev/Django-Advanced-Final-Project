from django import forms

from desserts.models import Dessert, Category, Ingredient


class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = '__all__'

        labels = {
            "name": "Dessert Name",
            "description": "Dessert Description",
            "price": "Dessert Price",
            "image": "Dessert Image",
            "category": "Dessert Category",
            "ingredients": "Ingredients Used",
        }

        help_texts = {
            "name": "Enter the name of the dessert.",
            "description": "Describe the dessert in detail.",
            "price": "Enter the price in EUR.",
            "image": "Upload an image of the dessert.",
            "category": "Select the category for this dessert.",
            "ingredients": "Select the ingredients used in this dessert.",
            "is_available": "Uncheck if this dessert is currently unavailable.",
        }

        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Please enter Dessert Description",
            }),
            "name": forms.TextInput(attrs={
                "placeholder": "Please enter Dessert Name",
            }),
            "price": forms.TextInput(attrs={
                "placeholder": "Please enter the price of the dessert in euro",
            }),
            "ingredients": forms.CheckboxSelectMultiple(),
        }

        error_messages = {
            "name": {
                "required": "Please enter a dessert name.",
                "max_length": "Dessert name cannot exceed 100 characters.",
                "unique": "A dessert with this name already exists.",
            },
            "price": {
                "required": "Please enter a dessert price.",
                "min_value": "Price can't be a negative number",
            },
            "image": {
                "invalid": "Please upload a valid image file.",
            }
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    labels = {
        "name": "Category Name",
        "description": "Category Description",
    }

    widgets = {
        "description": forms.Textarea(attrs={"rows": 3}),
    }

    error_messages = {
        "name": {
            "required": "Please enter a category name.",
        }
    }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

    labels = {
        "name": "Ingredient Name",
        "is_allergen": "Contains Allergen",
    }

    widgets = {
        "name": forms.TextInput(attrs={
            "placeholder": "Enter ingredient name",
        }),
        "is_allergen": forms.CheckboxInput(),
    }

    error_messages = {
        "name": {
            "required": "Please enter an ingredient name.",
        }
    }
