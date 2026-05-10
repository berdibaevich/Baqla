from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _


class TelegramGroup(models.Model):
    class DayType(models.TextChoices):
        ODD_DAYS = 'ODD', 'Odd Days (Mon/Wed/Fri)' 
        EVEN_DAYS = 'EVEN', 'Even Days (Tue/Thu/Sat)'

    class TimeSlot(models.TextChoices):
        AFTERNOON_1 = '14:00', '14:00'
        AFTERNOON_2 = '16:00', '16:00'
    

    days = models.CharField(_("Lesson Days"), max_length=4, choices=DayType.choices)
    time = models.CharField(_("Lesson Time"), max_length=5, choices=TimeSlot.choices)

    telegram_group_id = models.BigIntegerField(
        _("Telegram Group ID"),
        unique=True
    )

    # Status
    is_full = models.BooleanField(_("Is Full"), default=False)
    is_active_group = models.BooleanField(
        _("Is Active Group"),
        default=False,
        help_text="Barliq oqiwshi hám ata-analar toliq dizimnen ótken be?"
    )

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

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



class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE', _('Male')
        FEMALE = 'FEMALE', _('Female')
        NOT_SET = 'NOT_SET', _('Not Set')

    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"), unique=True, null=False, db_index=True)
    full_name = models.CharField(_("Full Name"), max_length=255)

    group = models.ForeignKey(
        'students.TelegramGroup',
        on_delete=models.SET_NULL,
        null=True,
        related_name="students",
        verbose_name=_("Class Group")
    )

    gender = models.CharField(
        _("Gender"),
        max_length=10,
        choices=Gender.choices,
        default=Gender.NOT_SET
    )

    phone_number = models.CharField(
        _("Phone Number"), 
        unique=True,
        max_length=13, 
        blank=True, 
        null=True
    )

    status = models.CharField(
        _("Status"),
        max_length=15, 
        choices=[
            ('pending', _('Pending')), 
            ('rejected', _('Rejected')), 
            ('approved', _('Approved')),
            ('inactive', _('Inactive')) # Kurstan shıqqanlar (Qoyǵanlar)
        ],
        default='pending'
    )

    # GitHub profile
    github_username = models.CharField(
        _("GitHub Username"),
        max_length=100, 
        unique=True
        )
    github_avatar_url = models.URLField(_("Avatar URL"), blank=True)
    github_profile_url = models.URLField(_("Profile URL"), blank=True)
    github_last_synced = models.DateTimeField(
        _("Last Synced with GitHub"), 
        null=True, 
        blank=True
    )

    # Parent Info
    parent_name = models.CharField(_("Parent Name"), max_length=20, blank=True)
    parent_phone_number = models.CharField(
        _("Parent Phone Number"),
        unique=True,
        max_length=13, 
        blank=True, 
        null=True
    )
    parent_telegram_id = models.BigIntegerField(
        _("Parent Telegram ID"), 
        null=True, 
        blank=True
    )
    is_parent_verified = models.BooleanField(_("Is Parent Verified"), default=False)

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)


    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


    def __str__(self):
        return "Student"
