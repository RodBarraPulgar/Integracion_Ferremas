import random
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime
from accounts.models import User
from sales.models import Sale, SaleItem
from inventory.models import Product

class Command(BaseCommand):
    help = 'Create sample sales for the users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        products = Product.objects.all()

        for user in users:
            number_of_sales = random.randint(1, 5)
            for _ in range(number_of_sales):
                sale_date = make_aware(datetime(2024, random.randint(1, 5), random.randint(1, 28)))
                sale = Sale.objects.create(
                    user=user,
                    date=sale_date,
                    total_amount=0,  # Placeholder, will be updated later
                )

                number_of_items = random.randint(1, 5)
                total_amount = 0

                for _ in range(number_of_items):
                    product = random.choice(products)
                    quantity = random.randint(1, 5)  # Adjust quantity as needed
                    price = product.price_clp
                    total_amount += price * quantity

                    SaleItem.objects.create(
                        sale=sale,
                        product=product,
                        quantity=quantity,
                        price=price,
                    )

                sale.total_amount = total_amount
                sale.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully created sale {sale.id} for user {user.username}'))