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



class DayType(models.TextChoices):
    ODD_DAYS = 'ODD', _('Odd Days (Mon/Wed/Fri)')
    EVEN_DAYS = 'EVEN', _('Even Days (Tue/Thu/Sat)')



class TimeSlot(models.TextChoices):
    MORNING_1 = '09:00', '09:00'
    MORNING_2 = '11:00', '11:00'
    AFTERNOON_1 = '14:00', '14:00'
    AFTERNOON_2 = '16:00', '16:00'
    EVENING_1 = '18:00', '18:00'



class Status(models.TextChoices):
    PENDING = 'pending', _('Pending')
    APPROVED = 'approved', _('Approved')
    REJECTED = 'rejected', _('Rejected')
    DROPPED_OUT = 'dropped_out', _('Dropped Out') # Kurstan shıqqanlar (Qoyǵanlar)



class RelationshipType(models.TextChoices):
    FATHER = 'FATHER', _('Father')
    MOTHER = 'MOTHER', _('Mother')
    GUARDIAN = 'GUARDIAN', _('Guardian')