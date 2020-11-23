from django.contrib import admin
from apps.administration.models import Offices, OfficeContacts


@admin.register(Offices)
class OfficesAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city", "address")
    ordering = '-created',
    list_filter = ["country"]
    search_fields = ('name',)


@admin.register(OfficeContacts)
class OfficeContactsAdmin(admin.ModelAdmin):
    list_display = ("office", "name", "main_contact", "email", "phone_prefix", "is_deleted")
    ordering = '-created',
    list_filter = ["office"]
    search_fields = ('name',)

    def phone_prefix(self, obj):
        return "{}{}".format(obj.phone_prefix, obj.phone)