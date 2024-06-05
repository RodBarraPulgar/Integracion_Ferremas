from django.core.management.base import BaseCommand
from inventory.models import Category, Product

class Command(BaseCommand):
    help = 'Populate the inventory with sample data'

    def handle(self, *args, **kwargs):
        categories = [
            {"pk": 1, "name": "Herramientas Manuales"},
            {"pk": 2, "name": "Herramientas Eléctricas"},
        ]

        products = [
            {"pk": 1, "name": "Martillo", "description": "Martillo de carpintero de 16 onzas", "price_clp": 12, "stock": 150, "category_id": 1, "image": "path_to_image"},
            {"pk": 2, "name": "Destornillador", "description": "Destornillador de estrella", "price_clp": 59, "stock": 200, "category_id": 1, "image": "path_to_image"},
            {"pk": 3, "name": "Alicate", "description": "Alicate universal", "price_clp": 8500, "stock": 18, "category_id": 1, "image": "path_to_image"},
            {"pk": 4, "name": "Llave Inglesa", "description": "Llave inglesa ajustable", "price_clp": 15, "stock": 130, "category_id": 1, "image": "path_to_image"},
            {"pk": 5, "name": "Taladro", "description": "Taladro eléctrico de 600W", "price_clp": 65000, "stock": 120, "category_id": 2, "image": "path_to_image"},
            {"pk": 6, "name": "Sierra Circular", "description": "Sierra circular de 1400W", "price_clp": 12, "stock": 110, "category_id": 2, "image": "path_to_image"},
            {"pk": 7, "name": "Lijadora", "description": "Lijadora orbital", "price_clp": 45, "stock": 140, "category_id": 2, "image": "path_to_image"},
            {"pk": 8, "name": "Atornillador Eléctrico", "description": "Atornillador eléctrico recargable", "price_clp": 25, "stock": 160, "category_id": 2, "image": "path_to_image"},
            {"pk": 9, "name": "Pistola de Calor", "description": "Pistola de calor de 2000W", "price_clp": 30, "stock": 190, "category_id": 2, "image": "path_to_image"},
            {"pk": 10, "name": "Nivel Láser", "description": "Nivel láser de precisión", "price_clp": 50, "stock": 150, "category_id": 2, "image": "path_to_image"},
            {"pk": 11, "name": "Cortadora de Césped", "description": "Cortadora de césped eléctrica", "price_clp": 20, "stock": 130, "category_id": 2, "image": "path_to_image"},
            {"pk": 12, "name": "Motocultor", "description": "Motocultor de 3.5 HP", "price_clp": 30, "stock": 120, "category_id": 2, "image": "path_to_image"},
            {"pk": 13, "name": "Cortadora de Azulejos", "description": "Cortadora de azulejos eléctrica", "price_clp": 150000, "stock": 110, "category_id": 2, "image": "path_to_image"},
            {"pk": 14, "name": "Generador Eléctrico", "description": "Generador eléctrico de 5000W", "price_clp": 40, "stock": 100, "category_id": 2, "image": "path_to_image"},
            {"pk": 15, "name": "Multímetro Digital", "description": "Multímetro digital de precisión", "price_clp": 20, "stock": 150, "category_id": 2, "image": "path_to_image"},
            {"pk": 16, "name": "Compresor de Aire", "description": "Compresor de aire de 2 HP", "price_clp": 25, "stock": 130, "category_id": 2, "image": "path_to_image"},
            {"pk": 17, "name": "Soldadora Inverter", "description": "Soldadora inverter de 200A", "price_clp": 18, "stock": 110, "category_id": 2, "image": "path_to_image"},
            {"pk": 18, "name": "Pistola de Pintura", "description": "Pistola de pintura eléctrica", "price_clp": 70, "stock": 140, "category_id": 2, "image": "path_to_image"},
            {"pk": 19, "name": "Caladora", "description": "Caladora eléctrica de 500W", "price_clp": 60, "stock": 170, "category_id": 2, "image": "path_to_image"},
            {"pk": 20, "name": "Lijadora de Banda", "description": "Lijadora de banda de 600W", "price_clp": 80, "stock": 160, "category_id": 2, "image": "path_to_image"},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(id=category_data["pk"], defaults={"name": category_data["name"]})
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created category {category.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category {category.name} already exists'))

        for product_data in products:
            try:
                category = Category.objects.get(pk=product_data["category_id"])
                product, created = Product.objects.get_or_create(
                    id=product_data["pk"],
                    defaults={
                        "name": product_data["name"],
                        "description": product_data["description"],
                        "price_clp": product_data["price_clp"],  # Cambiado a CLP y sin decimales
                        "stock": product_data["stock"],
                        "category": category,
                        "image": product_data["image"],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created product {product.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Product {product.name} already exists'))
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Category with id {product_data["category_id"]} does not exist'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the inventory with sample data'))
