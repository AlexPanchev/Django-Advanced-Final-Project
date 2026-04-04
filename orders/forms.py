from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem
from desserts.models import Dessert
from django.core.validators import RegexValidator


class OrderCreateForm(forms.ModelForm):
    customer_country_code = forms.CharField(
        max_length=5,
        required=True,
        validators=[RegexValidator(regex=r'^\+[0-9]{1,4}$', message="Country code must start with + and be 1-4 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "+359"})
    )
    customer_phone_number = forms.CharField(
        max_length=9,
        required=True,
        validators=[RegexValidator(regex=r'^[0-9]{9}$', message="Phone number must be exactly 9 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "123456789"})
    )
    class Meta:
        model = Order
        fields = ["customer_name", "customer_country_code", "customer_phone_number", "customer_email", "notes"]

    labels = {
        "customer_name": "Customer Name",
        "customer_country_code": "Country Code",
        "customer_phone_number": "Phone Number",
        "customer_email": "Email Address",
    }

    widgets = {
        "customer_country_code": forms.TextInput(attrs={"placeholder": "+359"}),
        "customer_phone_number": forms.TextInput(attrs={"placeholder": "123456789"}),
    }

    help_texts = {
        "customer_name": "Enter the customer's full name.",
        "customer_country_code": "Enter the country code (e.g., +359).",
        "customer_phone_number": "Enter the 9-digit phone number.",
        "customer_email": "Enter a valid email address.",
    }

    error_messages = {
        "customer_name": {
            "required": "Please enter the customer's name.",
            "max_length": "Customer name cannot exceed 100 characters.",
        },
        "customer_country_code": {
            "required": "Please enter a country code.",
        },
        "customer_phone_number": {
            "required": "Please enter a phone number.",
        },
        "customer_email": {
            "required": "Please enter an email address.",
            "invalid": "Please enter a valid email address.",
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        instance = super().save(commit=False)
        country_code = self.cleaned_data.get("customer_country_code")
        phone_number = self.cleaned_data.get("customer_phone_number")
        instance.customer_phone = f"{country_code} {phone_number}"
        if commit:
            instance.save()
        return instance


class OrderForm(forms.ModelForm):
    customer_country_code = forms.CharField(
        max_length=5,
        required=True,
        validators=[RegexValidator(regex=r'^\+[0-9]{1,4}$', message="Country code must start with + and be 1-4 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "+359"})
    )
    customer_phone_number = forms.CharField(
        max_length=9,
        required=True,
        validators=[RegexValidator(regex=r'^[0-9]{9}$', message="Phone number must be exactly 9 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "123456789"})
    )
    class Meta:
        model = Order
        fields = ["customer_name", "customer_country_code", "customer_phone_number", "customer_email", "status", "notes"]

    labels = {
        "customer_name": "Customer Name",
        "customer_country_code": "Country Code",
        "customer_phone_number": "Phone Number",
        "customer_email": "Email Address",
        "status": "Order Status",
    }

    widgets = {
        "customer_country_code": forms.TextInput(attrs={"placeholder": "+359"}),
        "customer_phone_number": forms.TextInput(attrs={"placeholder": "123456789"}),
    }

    help_texts = {
        "customer_name": "Enter the customer's full name.",
        "customer_country_code": "Enter the country code (e.g., +359).",
        "customer_phone_number": "Enter the 9-digit phone number.",
        "customer_email": "Enter a valid email address.",
        "status": "Select the current status of the order.",
    }

    error_messages = {
        "customer_name": {
            "required": "Please enter the customer's name.",
            "max_length": "Customer name cannot exceed 100 characters.",
        },
        "customer_country_code": {
            "required": "Please enter a country code.",
        },
        "customer_phone_number": {
            "required": "Please enter a phone number.",
        },
        "customer_email": {
            "required": "Please enter an email address.",
            "invalid": "Please enter a valid email address.",
        },
        "status": {
            "required": "Please select an order status.",
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({"class": "form-control"})
        # Populate fields from customer_phone
        if self.instance and self.instance.customer_phone:
            parts = self.instance.customer_phone.split(' ', 1)
            if len(parts) == 2 and parts[0].startswith('+'):
                self.fields['customer_country_code'].initial = parts[0]
                self.fields['customer_phone_number'].initial = parts[1].replace(' ', '')

    def save(self, commit=True):
        instance = super().save(commit=False)
        country_code = self.cleaned_data.get("customer_country_code")
        phone_number = self.cleaned_data.get("customer_phone_number")
        instance.customer_phone = f"{country_code} {phone_number}"
        if commit:
            instance.save()
        return instance


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
