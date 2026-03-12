from django.shortcuts import render, get_object_or_404, redirect

from .forms import DessertForm, CategoryForm, IngredientForm
from .models import Dessert, Category, Ingredient
from django.core.paginator import Paginator



# Create your views here.

def dessert_list(request):
    desserts = Dessert.objects.filter(is_available=True)
    paginator = Paginator(desserts, 8)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}
    return render(request, "desserts/dessert_list.html", context)

def all_desserts_list(request):
    desserts = Dessert.objects.all()
    paginator = Paginator(desserts, 8)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, "show_availability": True}
    return render(request, "desserts/all_desserts_list.html", context)

def dessert_detail(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    context = {"dessert": dessert}
    return render(request, "desserts/dessert_detail.html", context)

def dessert_create(request):
    if request.method == "POST":
        form = DessertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_desserts_list")
    else:
        form = DessertForm()

    context = {"form": form}
    return render(request, "desserts/dessert_form.html", context)

def dessert_edit(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)

    if request.method == "POST":
        form = DessertForm(request.POST, request.FILES, instance=dessert)
        if form.is_valid():
            form.save()
            return redirect("dessert_detail", pk=dessert.pk)
    else:
        form = DessertForm(instance=dessert)

    context = {"form": form, "dessert": dessert}
    return render(request, "desserts/dessert_form.html", context)

def dessert_delete(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)

    if request.method == "POST":
        dessert.delete()
        return redirect("dessert_list")

    context = {"dessert": dessert}
    return render(request, "desserts/dessert_delete.html", context)

def category_list(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories/category_list.html", context)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {"category": category}
    return render(request, "categories/category_detail.html", context)

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    context = {"form": form}
    return render(request, "categories/category_form.html", context)

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_detail", pk=category.pk)
    else:
        form = CategoryForm(instance=category)

    context = {
        "form": form,
        "category": category
    }

    return render(request, "categories/category_form.html", context)

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    context = {"category": category}
    return render(request, "categories/category_delete.html", context)

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    context = {"ingredients": ingredients}
    return render(request, "ingredients/ingredient_list.html", context)

def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    context = {"ingredient": ingredient}
    return render(request, "ingredients/ingredient_detail.html", context)

def ingredient_create(request):
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ingredient_list")
    else:
        form = IngredientForm()

    context = {"form": form}
    return render(request, "ingredients/ingredient_form.html", context)

def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect("ingredient_detail", pk=ingredient.pk)
    else:
        form = IngredientForm(instance=ingredient)

    context = {"form": form, "ingredient": ingredient}
    return render(request, "ingredients/ingredient_form.html", context)

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == "POST":
        ingredient.delete()
        return redirect("ingredient_list")

    context = {"ingredient": ingredient}
    return render(request, "ingredients/ingredient_delete.html", context)
