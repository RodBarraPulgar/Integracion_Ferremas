from django.contrib import admin
from .models import Sale, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

class SaleAdmin(admin.ModelAdmin):
    inlines = [SaleItemInline]
    list_display = ['id', 'user', 'date', 'total_amount']
    search_fields = ['user__username', 'date']

admin.site.register(Sale, SaleAdmin)
