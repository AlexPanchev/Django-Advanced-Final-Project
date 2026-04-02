from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from desserts.models import Dessert, Category, Ingredient
from orders.models import Order, OrderItem
from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def add_user_to_customers_group(sender, instance, created, **kwargs):
    if created:
        customers_group, _ = Group.objects.get_or_create(name="Customers")
        instance.groups.add(customers_group)


def create_default_groups():
    customers_group, _ = Group.objects.get_or_create(name="Customers")
    staff_group, _ = Group.objects.get_or_create(name="Staff")

    # Staff permissions: пълен контрол върху десерти, категории, съставки
    dessert_ct = ContentType.objects.get_for_model(Dessert)
    category_ct = ContentType.objects.get_for_model(Category)
    ingredient_ct = ContentType.objects.get_for_model(Ingredient)

    staff_permissions = Permission.objects.filter(
        content_type__in=[dessert_ct, category_ct, ingredient_ct]
    )
    staff_group.permissions.set(staff_permissions)

    # Customers permissions: работа с поръчки
    order_ct = ContentType.objects.get_for_model(Order)
    orderitem_ct = ContentType.objects.get_for_model(OrderItem)

    customer_permissions = Permission.objects.filter(
        content_type__in=[order_ct, orderitem_ct]
    )
    customers_group.permissions.set(customer_permissions)