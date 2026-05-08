from django import forms
from .models import GearRequest


class GearRequestForm(forms.ModelForm):
    class Meta:
        model = GearRequest
        fields = ['item_name', 'item_type', 'quantity', 'urgency', 'justification']
        widgets = {
            'justification': forms.Textarea(attrs={'rows': 4}),
        }
