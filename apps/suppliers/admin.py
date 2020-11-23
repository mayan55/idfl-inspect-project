from django.contrib import admin

from apps.suppliers.models import Suppliers, SupplierContacts, SupplierDocumentations


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ("name", "chinese_name", "country", "city", "nearest_idf_office", "is_deleted")
    ordering = '-created',
    list_filter = ["country", "city"]
    search_fields = ('name', 'identification_code', 'chinese_name')


@admin.register(SupplierContacts)
class SupplierContactsAdmin(admin.ModelAdmin):
    list_display = ("supplier", "main_contact", "name", "phone_prefix", "email", "is_deleted")
    ordering = '-created',
    list_filter = ["supplier"]
    search_fields = ('name',)

    def phone_prefix(self, obj):
        return "{}{}".format(obj.phone_prefix, obj.phone)


@admin.register(SupplierDocumentations)
class SupplierDocumentationsAdmin(admin.ModelAdmin):
    list_display = ("supplier", "type", "file")
    ordering = '-created',
    list_filter = ["type"]
    search_fields = ('file', 'type')
