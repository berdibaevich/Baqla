from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from ...utils import Role


class UserBaseManager(BaseUserManager):
    """Manager"""
    def create_superuser(self, phone_number, full_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_verified", True)
        other_fields.setdefault("role", Role.ADMIN)

        if not phone_number:
            raise ValueError("Failed: Phone number is required")

        if not full_name:
            raise ValueError("Failed: Full name is required")

        user = self.model(
            telegram_id=settings.SUPERUSER_TELEGRAM_ID,
            phone_number=phone_number,
            full_name = full_name,
            **other_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user



class UserBase(AbstractBaseUser, PermissionsMixin):
    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"), unique=True, null=False, db_index=True)
    full_name = models.CharField(_("Full name"), max_length=150, blank=True)
    phone_number = models.CharField(_("Phone number"), max_length=15, unique=True, blank=True, null=True)
    role = models.CharField(
        _("Role"),
        max_length=15,
        choices=Role.choices,
        default=Role.PENDING
    )
    
    # STATUS OF USER
    is_active = models.BooleanField(default=True) # If False, so was blocked
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(_("Is Verified"), default=False) # Will be verified by mentor

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserBaseManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return f"User #{self.id}"

