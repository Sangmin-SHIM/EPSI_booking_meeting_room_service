from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "user",
            "name",
            "room",
            "comment",
            "start_datetime",
            "end_datetime",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "room": forms.Select(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control"}),
            "start_datetime": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_datetime": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
        }
