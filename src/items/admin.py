from django.contrib import admin
from items.forms import ItemAdminForm
from items.models import Item, Location, Category, Material


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
