from django.urls import path
from .views import (
    DessertListView, AllDessertsListView, DessertDetailView,
    DessertCreateView, DessertUpdateView, DessertDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView,
    IngredientListView, IngredientDetailView, IngredientCreateView,
    IngredientUpdateView, IngredientDeleteView
)

urlpatterns = [
    path("", DessertListView.as_view(), name="dessert_list"),
    path("all/", AllDessertsListView.as_view(), name="all_desserts_list"),
    path("<int:pk>/", DessertDetailView.as_view(), name="dessert_detail"),
    path("create/", DessertCreateView.as_view(), name="dessert_create"),
    path("<int:pk>/edit/", DessertUpdateView.as_view(), name="dessert_edit"),
    path("<int:pk>/delete/", DessertDeleteView.as_view(), name="dessert_delete"),

    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),

    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient_detail"),
    path("ingredients/<int:pk>/edit/", IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient_delete"),
]