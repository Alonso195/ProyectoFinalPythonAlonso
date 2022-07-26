from django import forms

class ContactoFormulario(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()  
    message = forms.CharField()