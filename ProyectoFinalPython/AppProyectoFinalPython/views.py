
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView


from AppProyectoFinalPython.models import Contact, Proveedor
from AppProyectoFinalPython.forms import ContactFormulario, ProveedorFormulario

def inicio(self):
    return render(self, "inicio.html")

def contactUs(self):
    
    if (self.method == 'POST'):
        contactFormulario = ContactFormulario(self.POST)
        print(contactFormulario.is_valid())
        print(self.POST)
        if contactFormulario.is_valid():
            data = contactFormulario.cleaned_data
            contact = Contact(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
            contact.save()
            return render(self,'inicio.html')
    else:
        
        return render(self, "contactUs.html")

#------------------- PROVEEDORES VIEWS -------------------#
class ProveedorList(ListView):

    model = Proveedor
    template_name = './Proveedores/proveedor_list.html'
    context_object_name = 'Proveedores'

class ProveedorDetail(DetailView):

    model = Proveedor
    template_name = './Proveedores/proveedor_detail.html'
    context_object_name = 'Proveedor'

class ProveedorCreate(CreateView):
    model = Proveedor
    template_name = './Proveedores/proveedor_create.html'
    form_class: ProveedorFormulario
    fields = [ "Nombre", "Apellidos", "CodigoProveedor", "Cuit", "Provincia", "Localidad", "Direccion"]
    success_url = '/listaProveedores/' 


class ProveedorUpdate(UpdateView):

    model = Proveedor
    template_name = './Proveedores/proveedor_update.html'
    fields = ('__all__')
    success_url = '/listaProveedores/'

class ProveedorDelete(DeleteView):

    model = Proveedor
    template_name = './Proveedores/proveedor_delete.html'
    success_url = '/listaProveedores/'

