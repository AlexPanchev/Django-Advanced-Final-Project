from django.urls import path
from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path("add/<int:dessert_pk>/", ReviewCreateView.as_view(), name="review_add"),
    path("edit/<int:pk>/", ReviewUpdateView.as_view(), name="review_edit"),
    path("delete/<int:pk>/", ReviewDeleteView.as_view(), name="review_delete"),
]
