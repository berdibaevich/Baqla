import re
from django import forms
from src.utils import DayType, TimeSlot, RelationshipType


GITHUB_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
PHONE_RE = re.compile(r"^\+998\d{9}$")

DAY_LABELS_KAA = {
    DayType.ODD_DAYS: "Taq kúnler",
    DayType.EVEN_DAYS: "Jup kúnler",
}


RELATIONSHIP_LABELS_KAA = {
    RelationshipType.FATHER: "Ákesi",
    RelationshipType.MOTHER: "Anasi",
    RelationshipType.OTHER: "Basqa",
}


class StudentRegisterForm(forms.Form):
    days = forms.ChoiceField(
        label="Sabaq kúnleri", 
        choices=[(k, DAY_LABELS_KAA[k]) for k in DayType.values],
    )
    time = forms.ChoiceField(label="Sabaq waqti", choices=TimeSlot.choices)
    full_name = forms.CharField(label="Toliq ati", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Misali: Berdibaev Baxtiyar"}))
    github_username = forms.CharField(label="GitHub", max_length=39, widget=forms.TextInput(attrs={"placeholder": "Username"}))

    relationship = forms.ChoiceField(label="Kim?", choices=[(k, RELATIONSHIP_LABELS_KAA[k]) for k in RelationshipType.values])
    parent_name = forms.CharField(label="Ismi", max_length=100)
    parent_phone = forms.CharField(label="Telefon (+998...)", max_length=13)
