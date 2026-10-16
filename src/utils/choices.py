from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = 'MALE', _('Male')
    FEMALE = 'FEMALE', _('Female')
    NOT_SET = 'NOT_SET', _('Not Set')



class Role(models.TextChoices):
    ADMIN = 'ADMIN', _('Admin')
    MENTOR = 'MENTOR', _('Mentor')
    STUDENT = 'STUDENT', _('Student')
    PARENT = 'PARENT', _('Parent')
    PENDING = 'PENDING', _('Pending / Unverified')