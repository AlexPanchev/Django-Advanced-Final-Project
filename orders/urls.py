from django.urls import path
from .views import (
    OrderListView, OrderCreateView, OrderDetailView,
    OrderUpdateView, OrderDeleteView,
    OrderItemCreateView, OrderItemUpdateView, OrderItemDeleteView, MyOrdersView
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("<int:pk>/edit/", OrderUpdateView.as_view(), name="order_update"),
    path("<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),

    path("<int:order_pk>/add-item/", OrderItemCreateView.as_view(), name="orderitem_create"),
    path("item/<int:pk>/edit/", OrderItemUpdateView.as_view(), name="orderitem_update"),
    path("item/<int:pk>/delete/", OrderItemDeleteView.as_view(), name="orderitem_delete"),
    path("my-orders/", MyOrdersView.as_view(), name="my_orders"),

]