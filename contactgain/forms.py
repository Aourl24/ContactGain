from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={'type':'tel','value':'+234'}))
	class Meta:
		model = Contact
		fields = ['phone']