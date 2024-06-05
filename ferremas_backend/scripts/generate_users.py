import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremas_backend.settings')
django.setup()

User = get_user_model()

def create_users():
    for i in range(1, 11):
        username = f'user{i}'
        email = f'user{i}@example.com'
        password = 'password123'
        User.objects.create_user(username=username, email=email, password=password)

if __name__ == '__main__':
    create_users()
