from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem
from desserts.models import Dessert


class OrderCreateForm(forms.ModelForm):
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

    help_texts = {
        "customer_name": "Enter the customer's full name.",
        "customer_phone": "Enter a valid phone number (9-15 digits with optional country code).",
        "customer_email": "Enter a valid email address.",
    }

    error_messages = {
        "customer_name": {
            "required": "Please enter the customer's name.",
            "max_length": "Customer name cannot exceed 100 characters.",
        },
        "customer_phone": {
            "required": "Please enter a phone number.",
            "invalid": "Phone number must be 9-15 digits, optionally with a '+' prefix.",
            "max_length": "Phone number is too long.",
        },
        "customer_email": {
            "required": "Please enter an email address.",
            "invalid": "Please enter a valid email address.",
        }
    }


class OrderForm(forms.ModelForm):
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

    help_texts = {
        "customer_name": "Enter the customer's full name.",
        "customer_phone": "Enter a valid phone number (9-15 digits with optional country code).",
        "customer_email": "Enter a valid email address.",
        "status": "Select the current status of the order.",
    }

    error_messages = {
        "customer_name": {
            "required": "Please enter the customer's name.",
            "max_length": "Customer name cannot exceed 100 characters.",
        },
        "customer_phone": {
            "required": "Please enter a phone number.",
            "invalid": "Phone number must be 9-15 digits, optionally with a '+' prefix.",
            "max_length": "Phone number is too long.",
        },
        "customer_email": {
            "required": "Please enter an email address.",
            "invalid": "Please enter a valid email address.",
        },
        "status": {
            "required": "Please select an order status.",
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
            "unit_price": forms.NumberInput(attrs={"step": "0.01", "min": "0.01"}),
        }

        help_texts = {
            "dessert": "Select an available dessert for this order.",
            "quantity": "Enter the number of items to order.",
            "unit_price": "Enter the unit price in EUR.",
        }

        error_messages = {
            "dessert": {
                "required": "Please select a dessert.",
            },
            "quantity": {
                "required": "Please enter a quantity.",
                "min_value": "Quantity must be at least 1.",
            },
            "unit_price": {
                "required": "Please enter a unit price.",
                "min_value": "Unit price must be greater than zero.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dessert'].queryset = Dessert.objects.filter(is_available=True)
        self.fields['dessert'].help_text = "Select an available dessert."


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm, extra=1, min_num=1, validate_min=True
)
