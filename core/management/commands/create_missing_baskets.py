from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Basket

class Command(BaseCommand):
    help = 'Create baskets for users who do not have one.'

    def handle(self, *args, **options):
        User = get_user_model()
        created_count = 0
        for user in User.objects.all():
            if not hasattr(user, 'basket'):
                Basket.objects.create(user=user)
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f'Created {created_count} missing baskets.'))

