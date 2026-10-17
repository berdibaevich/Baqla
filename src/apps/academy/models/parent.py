from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import BaseModel
from src.utils import RelationshipType



class Parent(BaseModel):
    user = models.OneToOneField(
        'accounts.UserBase',
        on_delete=models.CASCADE,
        related_name='parent_profile'
    )
    relationship_type = models.CharField(
        _('Relationship Type'),
        max_length=10,
        choices=RelationshipType.choices,
        default=RelationshipType.MOTHER
    )
    student = models.ForeignKey(
        'academy.Student',
        on_delete=models.CASCADE,
        related_name='parents'
    )


    class Meta:
        db_table = 'parents'
        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'


    def __str__(self):
        return f"Parent #{self.id}"