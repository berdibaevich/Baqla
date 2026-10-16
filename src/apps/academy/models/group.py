from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from .base import BaseModel
from src.utils import DayType, TimeSlot



class TelegramGroup(BaseModel):
    days = models.CharField(_("Lesson Days"), max_length=4, choices=DayType.choices)
    time = models.CharField(_("Lesson Time"), max_length=5, choices=TimeSlot.choices)
    group_id = models.BigIntegerField(
        _("Telegram Group ID"),
        unique=True
    )

    # Status
    is_full = models.BooleanField(_("Is Full"), default=False)

    class Meta:
        db_table = 'telegram_group'
        verbose_name = _("Telegram Group")
        verbose_name_plural = _("Telegram Groups")

        constraints = [
            UniqueConstraint(
                fields=['days', 'time'], 
                name='unique_days_time_slot'
            )
        ]


    def __str__(self):
        return f"{self.get_days_display()} ({self.time})"