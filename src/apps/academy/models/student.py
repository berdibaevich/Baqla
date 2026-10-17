from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel
from src.utils import Gender, Status




class Student(BaseModel):
    user = models.OneToOneField(
        'accounts.UserBase',
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    group = models.ForeignKey(
        'academy.TelegramGroup',
        on_delete=models.SET_NULL,
        null=True,
        related_name="students"
    )

    gender = models.CharField(
        _("Gender"),
        max_length=10,
        choices=Gender.choices,
        default=Gender.NOT_SET
    )

    status = models.CharField(
        _("Status"),
        max_length=15, 
        choices=Status.choices,
        default=Status.PENDING
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


    class Meta:
        db_table = 'students'
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


    def __str__(self):
        return f"Student #{self.id}"