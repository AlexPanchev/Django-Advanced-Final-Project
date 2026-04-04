from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from orders.models import Order


def send_order_confirmation_email(order):
    subject = f"Order #{order.pk} Confirmation"
    message = f"Thank you for your order, {order.customer_name}!"
    recipient = order.customer_email

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient],
        fail_silently=False,
    )
def send_daily_order_report():
    today = timezone.now().date()
    orders = Order.objects.filter(created_at__date=today).count()

    subject = f"Daily order report - {today}"
    message = f"Total orders today: {orders}"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [admin_email for admin_email in [settings.DEFAULT_FROM_EMAIL]],
        fail_silently=True,
    )