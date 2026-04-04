from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class ProfileForm(forms.ModelForm):
    country_code = forms.CharField(
        max_length=5,
        required=False,
        validators=[RegexValidator(regex=r'^\+[0-9]{1,4}$', message="Country code must start with + and be 1-4 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "+359", "class": "form-control"}),
    )
    phone_number = forms.CharField(
        max_length=9,
        required=False,
        validators=[RegexValidator(regex=r'^[0-9]{9}$', message="Phone number must be exactly 9 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "123456789", "class": "form-control"}),
    )
    class Meta:
        model = Profile
        fields = ["avatar", "address", "birthdate", "preferred_allergens"]
        widgets = {
            "birthdate": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
            "preferred_allergens": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.phone:
            parts = self.instance.phone.split(' ', 1)
            if len(parts) == 2 and parts[0].startswith('+'):
                self.fields['country_code'].initial = parts[0]
                self.fields['phone_number'].initial = parts[1].replace(' ', '')

    def save(self, commit=True):
        instance = super().save(commit=False)
        country_code = self.cleaned_data.get('country_code', '')
        phone_number = self.cleaned_data.get('phone_number', '')
        if country_code and phone_number:
            instance.phone = f"{country_code} {phone_number}"
        else:
            instance.phone = ''
        if commit:
            instance.save()
        return instance

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    country_code = forms.CharField(
        max_length=5,
        required=True,
        validators=[RegexValidator(regex=r'^\+[0-9]{1,4}$', message="Country code must start with + and be 1-4 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "+359"})
    )
    phone_number = forms.CharField(
        max_length=9,
        required=True,
        validators=[RegexValidator(regex=r'^[0-9]{9}$', message="Phone number must be exactly 9 digits.")],
        widget=forms.TextInput(attrs={"placeholder": "123456789"})
    )
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        help_text="Select your date of birth."
    )

    class Meta:
        model = User
        fields = ["username", "email", "country_code", "phone_number", "birthdate", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to fields
        for field_name in self.fields:
            if field_name not in ["password1", "password2"]:
                self.fields[field_name].widget.attrs.update({"class": "form-control"})
        # Custom help text for password fields
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        
        if commit:
            user.save()
            # Create or update the profile with phone and birthdate
            profile, created = Profile.objects.get_or_create(user=user)
            country_code = self.cleaned_data.get("country_code")
            phone_number = self.cleaned_data.get("phone_number")
            profile.phone = f"{country_code} {phone_number}"
            profile.birthdate = self.cleaned_data.get("birthdate")
            profile.save()
        
        return user
