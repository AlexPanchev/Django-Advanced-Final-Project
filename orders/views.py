from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django_q.tasks import async_task

from .models import Order, OrderItem
from .forms import OrderForm, OrderCreateForm, OrderItemForm, OrderItemFormSet
from .tasks import send_order_confirmation_email


class OrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"
    permission_required = "orders.view_order"


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "orders/order_form.html"
    permission_required = "orders.add_order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["formset"] = OrderItemFormSet(self.request.POST)
        else:
            context["formset"] = OrderItemFormSet()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        async_task(send_order_confirmation_email, self.object)

        return response


class OrderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"
    permission_required = "orders.view_order"


class OrderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    permission_required = "orders.change_order"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.pk})


class OrderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/order_delete.html"
    success_url = reverse_lazy("order_list")
    permission_required = "orders.delete_order"


class OrderItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "orders/orderitem_form.html"
    permission_required = "orders.add_orderitem"

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


class MyOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/my_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CustomerOrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/customer_order_detail.html"
    context_object_name = "order"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CustomerOrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/order_delete.html"
    success_url = reverse_lazy("my_orders")

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, status=Order.Status.PENDING)


class OrderItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "orders/orderitem_form.html"
    permission_required = "orders.change_orderitem"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.order.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = self.object.order
        return context


class OrderItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = OrderItem
    template_name = "orders/orderitem_delete.html"
    permission_required = "orders.delete_orderitem"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.order.pk})