from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_number',
                    'creation_time', 'update_time', 'status'
                    ]
    list_display_links = ['table_number']
    list_filter = ['creation_time', 'status']
    inlines = [OrderItemInLine]

