from django.urls import path
from . import views

urlpatterns = [
    path("", views.dessert_list, name="dessert_list"),
    path("all/", views.all_desserts_list, name="all_desserts_list"),
    path("<int:pk>/", views.dessert_detail, name="dessert_detail"),
    path("create/", views.dessert_create, name="dessert_create"),
    path("<int:pk>/edit/", views.dessert_edit, name="dessert_edit"),
    path("<int:pk>/delete/", views.dessert_delete, name="dessert_delete"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<int:pk>/", views.category_detail, name="category_detail"),
    path("categories/<int:pk>/edit/", views.category_update, name="category_update"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),
]