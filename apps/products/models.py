from django.db import models
from apps.core.models import TimeStampedModel


class Category(TimeStampedModel):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = verbose_name
        db_table = "tbl_products_category"
        ordering = ["created"]

    name = models.CharField('Name', max_length=100)
    is_deleted = models.BooleanField('is deleted', default=False, blank=True)

    def __str__(self):
        return self.name


class SubCategory(TimeStampedModel):
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = verbose_name
        db_table = "tbl_products_sub_category"
        ordering = ["created"]

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=100)
    is_deleted = models.BooleanField('is deleted', default=False, blank=True)

    def __str__(self):
        return self.name


class ProductTypes(TimeStampedModel):
    class Meta:
        verbose_name = "ProductTypes"
        verbose_name_plural = verbose_name
        db_table = "tbl_products_product_types"
        ordering = ["created"]

    mou_type = [
        ('measure', "Measure"),
        ('unit', "Unit")
    ]

    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=100)
    mou = models.CharField("Measure of Unit", max_length=12, choices=mou_type)
    color = models.CharField('Color', max_length=12, blank=True, null=True)
    size = models.CharField('Size', max_length=12, blank=True, null=True)
    is_deleted = models.BooleanField('is deleted', default=False, blank=True)

    def __str__(self):
        return self.name

