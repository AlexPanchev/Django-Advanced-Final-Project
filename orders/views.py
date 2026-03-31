from django.shortcuts import render, redirect, get_object_or_404

from orders.forms import OrderForm, OrderCreateForm, OrderItemForm, OrderItemFormSet
from orders.models import Order, OrderItem

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.shortcuts import redirect

from .models import Order, OrderItem
from .forms import OrderForm, OrderCreateForm, OrderItemForm, OrderItemFormSet


class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "orders/order_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = OrderItemFormSet(self.request.POST)
        else:
            context["formset"] = OrderItemFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect("order_detail", pk=self.object.pk)

        return self.render_to_response(self.get_context_data(form=form))


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.pk})

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders/order_delete.html"
    success_url = reverse_lazy("order_list")

class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "orders/orderitem_form.html"

    def form_valid(self, form):
        order = Order.objects.get(pk=self.kwargs["order_pk"])
        item = form.save(commit=False)
        item.order = order
        item.save()
        return redirect("order_detail", pk=order.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = Order.objects.get(pk=self.kwargs["order_pk"])
        return context

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "orders/orderitem_form.html"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.order.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = self.object.order
        return context

class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = "orders/orderitem_delete.html"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.order.pk})