from django.db import models
from apps.core.models import TimeStampedModel


class Offices(TimeStampedModel):
    class Meta:
        verbose_name = "Offices"
        verbose_name_plural = verbose_name
        db_table = "tbl_offices"

    name = models.CharField('Name', max_length=100)
    country = models.CharField('Country', max_length=100)
    city = models.CharField('City', max_length=100)
    address = models.TextField('Address', blank=True, null=True)

    def __str__(self):
        return self.name


class OfficeContacts(TimeStampedModel):
    class Meta:
        verbose_name = "Office Contacts"
        verbose_name_plural = verbose_name
        db_table = "tbl_office_contacts"

    office = models.ForeignKey(Offices, on_delete=models.PROTECT)
    main_contact = models.BooleanField('Main Contact', blank=True, default=False)
    name = models.CharField('Name', max_length=100)
    phone_prefix = models.CharField('Phone Prefix', max_length=8)
    phone = models.CharField('Phone', max_length=24)
    mobile_phone_prefix = models.CharField('Mobile Phone Prefix', max_length=8, blank=True, null=True)
    mobile_phone = models.CharField('Mobile Phone', blank=True, null=True, max_length=24)
    email = models.EmailField('Email', blank=True, null=True)
    is_deleted = models.BooleanField('Is Deleted', default=False, blank=True)

    def __str__(self):
        return self.name