from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Dessert, Category, Ingredient
from .forms import DessertForm, CategoryForm, IngredientForm


class DessertListView(ListView):
    model = Dessert
    template_name = "desserts/dessert_list.html"
    paginate_by = 8

    def get_queryset(self):
        qs = Dessert.objects.filter(is_available=True)
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(name__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context



class AllDessertsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Dessert
    template_name = "desserts/all_desserts_list.html"
    paginate_by = 8
    permission_required = "desserts.view_dessert"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_availability"] = True
        return context


class DessertDetailView(DetailView):
    model = Dessert
    template_name = "desserts/dessert_detail.html"
    context_object_name = "dessert"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_has_reviewed'] = self.object.reviews.filter(user=self.request.user).exists()
        else:
            context['user_has_reviewed'] = False
        return context


class DessertCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Dessert
    form_class = DessertForm
    template_name = "desserts/dessert_form.html"
    success_url = reverse_lazy("all_desserts_list")
    permission_required = "desserts.add_dessert"


class DessertUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Dessert
    form_class = DessertForm
    template_name = "desserts/dessert_form.html"
    permission_required = "desserts.change_dessert"

    def get_success_url(self):
        return reverse_lazy("dessert_detail", kwargs={"pk": self.object.pk})


class DessertDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dessert
    template_name = "desserts/dessert_delete.html"
    success_url = reverse_lazy("dessert_list")
    permission_required = "desserts.delete_dessert"


class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("category_list")
    permission_required = "desserts.add_category"


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    permission_required = "desserts.change_category"

    def get_success_url(self):
        return reverse_lazy("category_detail", kwargs={"pk": self.object.pk})


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = "categories/category_delete.html"
    success_url = reverse_lazy("category_list")
    permission_required = "desserts.delete_category"


class IngredientListView(ListView):
    model = Ingredient
    template_name = "ingredients/ingredient_list.html"
    context_object_name = "ingredients"


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = "ingredients/ingredient_detail.html"
    context_object_name = "ingredient"


class IngredientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"
    success_url = reverse_lazy("ingredient_list")
    permission_required = "desserts.add_ingredient"


class IngredientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredients/ingredient_form.html"
    permission_required = "desserts.change_ingredient"

    def get_success_url(self):
        return reverse_lazy("ingredient_detail", kwargs={"pk": self.object.pk})


class IngredientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "ingredients/ingredient_delete.html"
    success_url = reverse_lazy("ingredient_list")
    permission_required = "desserts.delete_ingredient"