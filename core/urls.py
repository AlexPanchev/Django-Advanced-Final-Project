from django.urls import path
from .views import basket_view, add_to_basket, remove_from_basket, place_order_from_basket, increase_basket_item, decrease_basket_item

urlpatterns = [
    path('basket/', basket_view, name='basket_view'),
    path('basket/add/<int:dessert_id>/', add_to_basket, name='add_to_basket'),
    path('basket/remove/<int:item_id>/', remove_from_basket, name='remove_from_basket'),
    path('basket/increase/<int:item_id>/', increase_basket_item, name='increase_basket_item'),
    path('basket/decrease/<int:item_id>/', decrease_basket_item, name='decrease_basket_item'),
    path('basket/order/', place_order_from_basket, name='place_order_from_basket'),
]
# ...existing code...


