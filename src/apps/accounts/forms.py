import re
from django import forms
from src.utils import (
    DayType, 
    TimeSlot, 
    RelationshipType,
    DAY_LABELS_KAA,
    RELATIONSHIP_LABELS_KAA
)


PHONE_RE = re.compile(r"^\+998\d{9}$")


class StudentRegisterForm(forms.Form):
    days = forms.ChoiceField(
        label="Sabaq kúnleri", 
        choices=[(k, DAY_LABELS_KAA[k]) for k in DayType.values],
    )
    time = forms.ChoiceField(label="Sabaq waqti", choices=TimeSlot.choices)
    full_name = forms.CharField(label="Toliq ati", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Berdibayev Baxtiyar"}))
    github_username = forms.CharField(label="GitHub", max_length=39, widget=forms.TextInput(attrs={"placeholder": "Username"}))

    relationship = forms.ChoiceField(label="Kim?", choices=[(k, RELATIONSHIP_LABELS_KAA[k]) for k in RelationshipType.values])
    parent_name = forms.CharField(label="Ati", max_length=100)
    parent_phone = forms.CharField(
        label="Telefon", 
        max_length=13, 
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "placeholder": "+998901234567"
            }
        )
    )
