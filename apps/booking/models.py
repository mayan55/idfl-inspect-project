from django.contrib.auth.models import User
from django.db import models

from apps.booking.utils.vars import booking_types, booking_status
from apps.core.models import TimeStampedModel


class Bookings(TimeStampedModel):
    class Meta:
        verbose_name = "Bookings"
        verbose_name_plural = verbose_name
        db_table = "tbl_bookings"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_type = models.CharField('BookingType', max_length=100, choices=booking_types)
    status = models.CharField('Status', max_length=24, default="draft", choices=booking_status)
    # todo to be continued
