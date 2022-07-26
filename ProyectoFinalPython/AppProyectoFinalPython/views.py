
from django.shortcuts import render

from AppProyectoFinalPython.models import Contacto
from AppProyectoFinalPython.forms import ContactoFormulario

def inicio(self):
    return render(self, "inicio.html")

def contactUs(self):
    
    if (self.method == 'POST'):
        contactoFormulario = ContactoFormulario(self.POST)
        print(contactoFormulario.is_valid())
        print(self.POST)
        if contactoFormulario.is_valid():
            data = contactoFormulario.cleaned_data
            contacto = Contacto(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
            contacto.save()
            return render(self,'inicio.html')
    else:
        
        return render(self, "contactUs.html")
