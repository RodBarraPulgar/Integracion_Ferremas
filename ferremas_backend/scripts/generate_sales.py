import os
import django
import random
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremas_backend.settings')
django.setup()

from accounts.models import User
from inventory.models import Product
from sales.models import Sale, SaleItem

def create_sales():
    users = User.objects.all()
    products = Product.objects.all()

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 5, 31)

    current_date = start_date

    while current_date <= end_date:
        num_sales = random.randint(10, 30)
        for _ in range(num_sales):
            user = random.choice(users)
            sale = Sale.objects.create(
                user=user,
                date=make_aware(current_date + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))),
                total_amount=0
            )

            num_items = random.randint(1, 5)
            total_amount = 0

            for _ in range(num_items):
                product = random.choice(products)
                quantity = random.randint(1, 5)
                price = product.price_usd * quantity
                SaleItem.objects.create(
                    sale=sale,
                    product=product,
                    quantity=quantity,
                    price=price
                )
                total_amount += price

            sale.total_amount = total_amount
            sale.save()

        current_date += timedelta(days=1)

if __name__ == '__main__':
    create_sales()
