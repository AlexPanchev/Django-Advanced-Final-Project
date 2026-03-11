from django import forms
from .models import Order, OrderItem
from desserts.models import Dessert


class OrderCreateForm(forms.ModelForm):
    """Form for creating new orders - status is automatically set to PENDING"""
    class Meta:
        model = Order
        fields = ["customer_name", "customer_phone", "customer_email", "notes"]

    labels = {
        "customer_name": "Customer Name",
        "customer_phone": "Phone Number",
        "customer_email": "Email Address",
    }

    widgets = {
        "customer_phone": forms.TextInput(attrs={"placeholder": "e.g. +359 123 456 789"}),
    }

    error_messages = {
        "customer_name": {
            "required": "Please enter the customer's name.",
        },
        "customer_email": {
            "invalid": "Please enter a valid email address.",
        }
    }


class OrderForm(forms.ModelForm):
    """Form for updating existing orders - includes status field"""
    class Meta:
        model = Order
        fields = ["customer_name", "customer_phone", "customer_email", "status", "notes"]

    labels = {
        "customer_name": "Customer Name",
        "customer_phone": "Phone Number",
        "customer_email": "Email Address",
        "status": "Order Status",
    }

    widgets = {
        "customer_phone": forms.TextInput(attrs={"placeholder": "e.g. +359 123 456 789"}),
    }

    error_messages = {
        "customer_name": {
            "required": "Please enter the customer's name.",
        },
        "customer_email": {
            "invalid": "Please enter a valid email address.",
        }
    }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["dessert", "quantity", "unit_price"]

        labels = {
            "dessert": "Dessert",
            "quantity": "Quantity",
            "unit_price": "Unit Price",
        }

        widgets = {
            "quantity": forms.NumberInput(attrs={"min": 1}),
        }

        error_messages = {
            "quantity": {
                "required": "Please enter a quantity.",
                "min_value": "Quantity must be at least 1.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show available desserts
        self.fields['dessert'].queryset = Dessert.objects.filter(is_available=True)
        self.fields['dessert'].help_text = "Select an available dessert."
