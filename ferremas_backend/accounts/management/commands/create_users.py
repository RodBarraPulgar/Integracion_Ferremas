from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Create 11 sample users'

    def handle(self, *args, **kwargs):
        users_data = [
            {"username": "alexorell", "email": "user11@example.com", "password": "ManUtd69", "phone": "987654321", "address": "hugo bravo 511", "rut": "16629147-k"},
            {"username": "user1", "email": "user1@example.com", "password": "password1", "phone": "123456789", "address": "Address 1", "rut": "12345678-1"},
            {"username": "user2", "email": "user2@example.com", "password": "password2", "phone": "123456789", "address": "Address 2", "rut": "12345678-2"},
            {"username": "user3", "email": "user3@example.com", "password": "password3", "phone": "123456789", "address": "Address 3", "rut": "12345678-3"},
            {"username": "user4", "email": "user4@example.com", "password": "password4", "phone": "123456789", "address": "Address 4", "rut": "12345678-4"},
            {"username": "user5", "email": "user5@example.com", "password": "password5", "phone": "123456789", "address": "Address 5", "rut": "12345678-5"},
            {"username": "user6", "email": "user6@example.com", "password": "password6", "phone": "123456789", "address": "Address 6", "rut": "12345678-6"},
            {"username": "user7", "email": "user7@example.com", "password": "password7", "phone": "123456789", "address": "Address 7", "rut": "12345678-7"},
            {"username": "user8", "email": "user8@example.com", "password": "password8", "phone": "123456789", "address": "Address 8", "rut": "12345678-8"},
            {"username": "user9", "email": "user9@example.com", "password": "password9", "phone": "123456789", "address": "Address 9", "rut": "12345678-9"},
            {"username": "user10", "email": "user10@example.com", "password": "password10", "phone": "123456789", "address": "Address 10", "rut": "12345678-10"},
        ]

        for user_data in users_data:
            user = User.objects.create_user(
                username=user_data["username"],
                email=user_data["email"],
                password=user_data["password"],
                phone=user_data["phone"],
                address=user_data["address"],
                rut=user_data["rut"],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))