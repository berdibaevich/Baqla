from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models
from django.utils.translation import gettext_lazy as _


class UserBaseManager(BaseUserManager):
    """Custom Manager"""

    def create_superuser(self, telegram_id, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
    
        user = self.model(
            telegram_id = telegram_id,
            **other_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user



class UserBase(AbstractBaseUser, PermissionsMixin):
    telegram_id = models.PositiveBigIntegerField(_("Telegram ID"), unique=True, null=False, db_index=True)
    is_active = models.BooleanField(_("Active"), default=False)
    is_staff = models.BooleanField(_("Staff"), default=False)
    is_superuser = models.BooleanField(_("Superuser"), default=False)
    
    created_at = models.DateTimeField(
        auto_now_add= True,
        editable=False,
        verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        editable=False,
        verbose_name=_("Updated At"),
    )

    objects = UserBaseManager()
    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = []


    class Meta:
        db_table = 'user_base'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.telegram_id}"
    