from rest_framework.routers import DefaultRouter
from .views import (
    DessertViewSet, CategoryViewSet, IngredientViewSet,
    ReviewViewSet, OrderViewSet
)

router = DefaultRouter()
router.register("desserts", DessertViewSet)
router.register("categories", CategoryViewSet)
router.register("ingredients", IngredientViewSet)
router.register("reviews", ReviewViewSet)
router.register("orders", OrderViewSet)

urlpatterns = router.urls
