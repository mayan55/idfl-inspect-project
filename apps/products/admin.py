from django.contrib import admin
from apps.products.models import Category, SubCategory, ProductTypes


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_deleted", "created")
    ordering = '-created',


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_deleted", "created")
    ordering = '-created',
    list_filter = ["category"]
    search_fields = ('name',)


@admin.register(ProductTypes)
class ProductTypesAdmin(admin.ModelAdmin):
    list_display = ("category", "sub_category", "name", "mou", "color", "size", "is_deleted")
    ordering = '-created',
    list_filter = ["sub_category", "mou", "color", "size"]
    search_fields = ('sub_category', 'name')

    def category(self, obj):
        return obj.sub_category.category