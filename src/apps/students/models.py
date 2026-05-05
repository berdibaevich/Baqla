from django.db import models
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
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_full = models.BooleanField(_("Is Full"), default=False, editable=False)

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        db_table = 'telegram_group'
        verbose_name = _("Telegram Group")
        verbose_name_plural = _("Telegram Groups")


    def __str__(self):
        return f"{self.days} ({self.time})"



class Student(models.Model):
    user = models.OneToOneField(
        "users.UserBase",
        on_delete=models.CASCADE,
        related_name="student_profile",
        verbose_name=_("User Account")
    )

    group = models.ForeignKey(
        'students.TelegramGroup',
        on_delete=models.SET_NULL,
        null=True,
        related_name="students",
        verbose_name=_("Class Group")
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
    parent_full_name = models.CharField(_("Parent Full Name"), max_length=200, blank=True)
    parent_telegram_id = models.BigIntegerField(
        _("Parent Telegram ID"), 
        null=True, 
        blank=True
    )
    is_parent_verified = models.BooleanField(_("Is Parent Verified"), default=False)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


    def __str__(self):
        return "Student"







