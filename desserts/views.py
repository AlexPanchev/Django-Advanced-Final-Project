from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import Dessert, Category, Ingredient
from .forms import DessertForm, CategoryForm, IngredientForm


# Create your views here.

class DessertListView(ListView):
    model = Dessert
    template_name = "desserts/dessert_list.html"
    paginate_by = 8

    def get_queryset(self):
        return Dessert.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_obj"] = context["page_obj"]
        return context

class AllDessertsListView(ListView):
    model = Dessert
    template_name = "desserts/all_desserts_list.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_availability"] = True
        context["page_obj"] = context["page_obj"]
        return context

class DessertDetailView(DetailView):
    model = Dessert
    template_name = "desserts/dessert_detail.html"
    context_object_name = "dessert"

class DessertCreateView(CreateView):
    model = Dessert
    form_class = DessertForm
    template_name = "desserts/dessert_form.html"
    success_url = reverse_lazy("all_desserts_list")

class DessertUpdateView(UpdateView):
    model = Dessert
    form_class = DessertForm
    template_name = "desserts/dessert_form.html"

    def get_success_url(self):
        return reverse_lazy("dessert_detail", kwargs={"pk": self.object.pk})

class DessertDeleteView(DeleteView):
    model = Dessert
    template_name = "desserts/dessert_delete.html"
    success_url = reverse_lazy("dessert_list")

class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"

    def get_success_url(self):
        return reverse_lazy("category_detail", kwargs={"pk": self.object.pk})

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category_delete.html"
    success_url = reverse_lazy("category_list")

class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredients/ingredient_list.html"
    context_object_name = "ingredients"

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "ingredients/ingredient_detail.html"
    context_object_name = "ingredient"

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"
    success_url = reverse_lazy("ingredient_list")

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"

    def get_success_url(self):
        return reverse_lazy("ingredient_detail", kwargs={"pk": self.object.pk})

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredients/ingredient_delete.html"
    success_url = reverse_lazy("ingredient_list")
