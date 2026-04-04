from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from desserts.models import Dessert
from .models import Basket, BasketItem
from orders.models import Order, OrderItem
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def basket_view(request):
    basket = request.user.basket
    items = basket.items.select_related('dessert')
    return render(request, 'core/basket.html', {'basket': basket, 'items': items})

@login_required
def add_to_basket(request, dessert_id):
    basket = request.user.basket
    dessert = get_object_or_404(Dessert, pk=dessert_id, is_available=True)
    item, created = BasketItem.objects.get_or_create(basket=basket, dessert=dessert)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f"Added {dessert.name} to your basket.")
    return redirect('basket_view')

@login_required
def remove_from_basket(request, item_id):
    basket = request.user.basket
    item = get_object_or_404(BasketItem, pk=item_id, basket=basket)
    item.delete()
    messages.success(request, "Item removed from basket.")
    return redirect('basket_view')

@login_required
def place_order_from_basket(request):
    basket = request.user.basket
    items = basket.items.select_related('dessert')
    if not items.exists():
        messages.error(request, "Your basket is empty.")
        return redirect('basket_view')
    order = Order.objects.create(
        user=request.user,
        customer_name=request.user.profile.user.username,
        customer_phone=request.user.profile.phone or '',
        customer_email=request.user.email,
        status=Order.Status.PENDING,
    )
    for item in items:
        OrderItem.objects.create(
            order=order,
            dessert=item.dessert,
            quantity=item.quantity,
            unit_price=item.dessert.price,
        )
    items.delete()  # Clear basket
    messages.success(request, "Order placed successfully!")
    return redirect('my_orders')

@login_required
def increase_basket_item(request, item_id):
    basket = request.user.basket
    item = get_object_or_404(BasketItem, pk=item_id, basket=basket)
    item.quantity += 1
    item.save()
    messages.success(request, f"Updated quantity for {item.dessert.name}.")
    return redirect('basket_view')

@login_required
def decrease_basket_item(request, item_id):
    basket = request.user.basket
    item = get_object_or_404(BasketItem, pk=item_id, basket=basket)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        messages.success(request, f"Updated quantity for {item.dessert.name}.")
    else:
        item.delete()
        messages.success(request, "Item removed from basket.")
    return redirect('basket_view')
