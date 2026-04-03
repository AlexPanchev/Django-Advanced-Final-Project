from rest_framework import viewsets, permissions
from desserts.models import Dessert, Category, Ingredient
from orders.models import Order, OrderItem
from reviews.models import Review

from .serializers import (
    DessertSerializer, CategorySerializer, IngredientSerializer,
    OrderSerializer, OrderItemSerializer, ReviewSerializer
)


class DessertViewSet(viewsets.ModelViewSet):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
