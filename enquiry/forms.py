from .models import EnquiryRequest
from django import forms

class EnquiryRequestForm(forms.ModelForm):
    class Meta:
        model= EnquiryRequest
        fields = ('name', 'email','subject', 'message')