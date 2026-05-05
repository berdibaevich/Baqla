from django.db import models
from django.utils.translation import gettext_lazy as _


class TelegramGroup(models.Model):
    class DayType(models.TextChoices):
        ODD_DAYS = 'ODD', 'Odd Days (Mon/Wed/Fri)' 
        EVEN_DAYS = 'EVEN', 'Even Days (Tue/Thu/Sat)'

    class TimeSlot(models.TextChoices):
        AFTERNOON_1 = '14:00', '14:00'
        AFTERNOON_2 = '16:00', '16:00'
    

    days = models.CharField(max_length=4, choices=DayType.choices)
    time = models.CharField(max_length=5, choices=TimeSlot.choices)

    telegram_group_id = models.BigIntegerField(
        _("Telegram Group ID"),
        unique=True
    )

    # Status
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_full = models.BooleanField(_("Is Full"), default=False, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'telegram_group'
        verbose_name = 'Telegram group'
        verbose_name_plural = 'Telegram groups'


    def __str__(self):
        return f"{self.days} ({self.time})"

