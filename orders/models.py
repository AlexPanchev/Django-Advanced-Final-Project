from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from desserts.models import Dessert

# Phone number validator
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
)


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        COMPLETED = 'Completed', 'Completed'
        CONFIRMED = 'Confirmed', 'Confirmed'


    customer_name = models.CharField(
        max_length=100,
        verbose_name='Customer Name',
        )
    customer_phone = models.CharField(
        max_length=17,
        validators=[phone_regex],
        help_text='Enter a valid phone number (e.g., +359 123 456 789).',
    )
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(
        blank=True,
        help_text='Optional notes for the order',
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name='Order Status',
    )

    def __str__(self):
        return f"{self.customer_name} ({self.status})"

    def total_price(self):
        return sum(item.line_total() for item in self.items.all())

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-created_at"]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, related_name='order_items')

    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantity",
        help_text="Enter the number of items.",
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    def __str__(self):
        return f"{self.quantity}x {self.dessert}"

    def line_total(self):
        return self.unit_price * self.quantity

    class Meta:
        ordering = ["order"]
