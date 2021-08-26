from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'text-right'}),
            'last_name': forms.TextInput(attrs={'class': 'text-right'}),
            'age': forms.NumberInput(attrs={'class': 'text-right'}),
        }


# class LeadForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=0)