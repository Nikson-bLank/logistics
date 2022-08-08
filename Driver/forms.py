from django import forms
from .models import Driver_Detail
class DriverForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Driver_Detail