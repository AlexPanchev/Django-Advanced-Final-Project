from django.shortcuts import render, redirect, get_object_or_404

from orders.forms import OrderForm, OrderCreateForm, OrderItemForm
from orders.models import Order, OrderItem


# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    context = {"orders": orders}

    return render(request, "orders/order_list.html", context)

def order_create(request):
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderCreateForm()
    context = {"form": form}
    return render(request, "orders/order_form.html", context)


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "orders/order_detail.html", {"order": order})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderForm(instance=order)

    return render(request, "orders/order_form.html", {"form": form, "order": order})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        order.delete()
        return redirect("order_list")

    context = {"order": order}
    return render(request, "orders/order_delete.html", context)

def orderitem_create(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)

    if request.method == "POST":
        form = OrderItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.order = order
            item.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderItemForm()
    context = {
        "form": form,
        "order": order
    }

    return render(request, "orders/orderitem_form.html", context)

def orderitem_update(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    order = item.order

    if request.method == "POST":
        form = OrderItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderItemForm(instance=item)

    return render(request, "orders/orderitem_form.html", {"form": form, "order": order})

def orderitem_delete(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    order = item.order

    if request.method == "POST":
        item.delete()
        return redirect("order_detail", pk=order.pk)

    return render(request, "orders/orderitem_delete.html", {"item": item})