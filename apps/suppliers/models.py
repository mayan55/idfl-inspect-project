from django.contrib.auth.models import User
from django.db import models

from apps.administration.models import Offices
from apps.core.models import TimeStampedModel
from apps.products.models import ProductTypes
from apps.suppliers.utils.vars import documentation_types, sale_turnover, number_of_employees


class Suppliers(TimeStampedModel):
    class Meta:
        verbose_name = "Suppliers"
        verbose_name_plural = verbose_name
        db_table = "tbl_suppliers_suppliers"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=100)
    identification_code = models.BigIntegerField('Identification Code', blank=True, null=True)
    chinese_name = models.CharField('Chinese Name', max_length=100, blank=True, null=True)
    main_product_lines = models.ManyToManyField(ProductTypes, blank=True)

    country = models.CharField('Country', max_length=100)
    city = models.CharField('City', max_length=100)
    address = models.TextField('Address')
    chinese_address = models.TextField('Chinese Address', blank=True, null=True)
    postal_code = models.CharField('Postal Code', max_length=12, blank=True, null=True)

    nearest_idf_office = models.ForeignKey(Offices, blank=True, null=True, on_delete=models.PROTECT)
    web_site = models.CharField('Website', max_length=200, blank=True, null=True)
    sales_turnover = models.CharField('Sales Turnover', blank=True, null=True, choices=sale_turnover, max_length=24)
    number_of_employees = models.CharField('Number Of Employees', blank=True, null=True, choices=number_of_employees, max_length=24)

    is_deleted = models.BooleanField('Is Deleted', default=False, blank=True)

    def __str__(self):
        return self.name


class SupplierContacts(TimeStampedModel):
    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = verbose_name
        db_table = "tbl_supplier_contacts"

    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    main_contact = models.BooleanField('Main Contact', blank=True, default=False)
    name = models.CharField('Name', max_length=100)
    phone_prefix = models.CharField('Phone Prefix', max_length=8)
    phone = models.CharField('Phone', max_length=24)
    mobile_phone_prefix = models.CharField('Mobile Phone Prefix', max_length=8, blank=True, null=True)
    mobile_phone = models.CharField('Mobile Phone', blank=True, null=True, max_length=24)
    email = models.EmailField('Email', blank=True, null=True)
    is_deleted = models.BooleanField('Is Deleted', default=False, blank=True)


class SupplierDocumentations(TimeStampedModel):
    class Meta:
        verbose_name = "Documentations"
        verbose_name_plural = verbose_name
        db_table = "tbl_supplier_documentations"

    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    type = models.CharField('Type', max_length=48, choices=documentation_types)
    file = models.FileField(upload_to='media/documentations/suppliers/')
