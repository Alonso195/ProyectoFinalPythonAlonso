from django import forms

class ContactFormulario(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()  
    message = forms.CharField()

class BookForm(forms.Form):
    name = forms.CharField()
    author = forms.CharField()
    genre = forms.CharField() 
    date = forms.DateField()


class AuthorForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()    
    born = forms.DateField()  

class ProveedorFormulario(forms.Form):
    CodigoProveedor = forms.CharField()
    Nombre = forms.CharField()
    Apellidos = forms.CharField()  
    Provincia = forms.CharField()  
    Localidad = forms.CharField()  
    Direccion = forms.CharField()  
    Cuit = forms.CharField()