from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models
from django.utils.translation import gettext_lazy as _


class UserBaseManager(BaseUserManager):
    """Custom Manager"""

    def create_superuser(self, telegram_id, full_name, password, **other_fields):
        other_fields.setdefault("role", self.model.Role.SUPERUSER)

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_verified", True)
    
        user = self.model(
            full_name = full_name,
            telegram_id = telegram_id,
            **other_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user



class UserBase(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        SUPERUSER = 'superuser', 'Superuser'
        STUDENT = 'student', 'Student'
        PARENT = 'parent', 'Parent'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    full_name = models.CharField(_("Full Name"), max_length=255)
    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"), unique=True, null=False, db_index=True)
    
    # STATUS OF USER
    is_active = models.BooleanField(_("Active"), default=False)
    is_staff = models.BooleanField(_("Staff"), default=False)
    is_superuser = models.BooleanField(_("Superuser"), default=False)
    is_verified = models.BooleanField(_("Verified"), default=False)
    
    created_at = models.DateTimeField(
        auto_now_add= True,
        editable=False,
        verbose_name=_("Date joined")
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        editable=False,
        verbose_name=_("Last update"),
    )

    objects = UserBaseManager()
    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = ['full_name']


    class Meta:
        db_table = 'user_base'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.full_name} ({self.role})"
    