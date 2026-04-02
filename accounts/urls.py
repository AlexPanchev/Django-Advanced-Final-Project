from django.urls import path
from .views import profile_detail, profile_edit, RegisterView

urlpatterns = [
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("register/", RegisterView.as_view(), name="register")
]