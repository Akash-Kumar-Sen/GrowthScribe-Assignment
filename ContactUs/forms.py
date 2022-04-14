from django import forms
from django.db import models
from .models import ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields=['name','email','details']

    def __init__(self, *args, **kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        #Charfields
        self.fields['name'].widget.attrs['type'] = 'text'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['details'].widget.attrs['type'] = 'text'
        
        self.fields['name'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['details'].widget.attrs['class'] = 'input'

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Full Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email Address'
        self.fields['details'].widget.attrs['placeholder'] = 'Enter Your Project Details'

        