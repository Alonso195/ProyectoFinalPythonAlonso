
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from AppProyectoFinalPython.models import Contact, Proveedor,Cliente,Articulo
from AppProyectoFinalPython.forms import ContactFormulario, ProveedorFormulario,ClienteFormulario,ArticuloFormulario

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

def buscarProveedor(request):
 

    if request.GET["codigo"]:

        codigo = request.GET["codigo"]

        Proveedores = Proveedor.objects.filter(CodigoProveedor__icontains=codigo)

        return render(request, "./Proveedores/proveedor_list.html", {"Proveedores": Proveedores, "codigo": codigo})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

def login_request(request):
    print('method:', request.method)
    print('post:', request.POST)
    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})

            else:

                return render(request, "login.html", {"mensaje": "Error, datos incorrectos"})

        return render(request, "login.html", {"mensaje": "Error, datos incorrectos"})

    else:

        miFormulario = AuthenticationForm()

    return render(request, "login.html", {"miFormulario": miFormulario})

#------------------- PROVEEDORES VIEWS -------------------#
class ProveedorList(LoginRequiredMixin, ListView):

    model = Proveedor
    template_name = './Proveedores/proveedor_list.html'
    context_object_name = 'Proveedores'

class ProveedorDetail(LoginRequiredMixin, DetailView):

    model = Proveedor
    template_name = './Proveedores/proveedor_detail.html'
    context_object_name = 'Proveedor'

class ProveedorCreate(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = './Proveedores/proveedor_create.html'
    form_class: ProveedorFormulario
    fields = [ "Nombre", "Apellidos", "CodigoProveedor", "Cuit", "Provincia", "Localidad", "Direccion"]
    success_url = '/listaProveedores/' 


class ProveedorUpdate(LoginRequiredMixin, UpdateView):

    model = Proveedor
    template_name = './Proveedores/proveedor_update.html'
    fields = ('__all__')
    success_url = '/listaProveedores/'

class ProveedorDelete(LoginRequiredMixin, DeleteView):

    model = Proveedor
    template_name = './Proveedores/proveedor_delete.html'
    success_url = '/listaProveedores/'

#------------------- CLIENTES VIEWS -------------------#

class ClienteList(LoginRequiredMixin, ListView):

    model = Cliente
    template_name = './Clientes/cliente_list.html'
    context_object_name = 'Clientes'

class ClienteDetail(LoginRequiredMixin, DetailView):

    model = Cliente
    template_name = './Clientes/cliente_detail.html'
    context_object_name = 'Cliente'

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = './Clientes/cliente_create.html'
    form_class: ClienteFormulario
    fields = [ "Nombre", "Apellidos", "CodigoCliente", "Cuit", "Provincia", "Localidad", "Direccion"]
    success_url = '/listaClientes/' 


class ClienteUpdate(LoginRequiredMixin, UpdateView):

    model = Cliente
    template_name = './Clientes/Cliente_update.html'
    fields = ('__all__')
    success_url = '/listaClientes/'

class ClienteDelete(LoginRequiredMixin, DeleteView):

    model = Cliente
    template_name = './Clientes/cliente_delete.html'
    success_url = '/listaClientes/'


# ---------------------------Articulos 

class ArticuloList(LoginRequiredMixin, ListView):

    model = Articulo
    template_name = './Articulos/Articulo_list.html'
    context_object_name = 'Articulos'

class ArticuloDetail(LoginRequiredMixin, DetailView):

    model = Articulo
    template_name = './Articulos/Articulos_detail.html'
    context_object_name = 'Articulos'

class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = './Articulos/Articulo_create.html'
    form_class: ArticuloFormulario
    fields = [ "CodigoArticulo", "Descripcion", "Color", "Talle", "Precio", "CodigoBarra"]
    success_url = '/listaArticulos/' 


class ArticuloUpdate(LoginRequiredMixin, UpdateView):

    model = Articulo
    template_name = './Articulos/Articulo_update.html'
    fields = ('__all__')
    success_url = '/listaArticulos/'

class ArticuloDelete(LoginRequiredMixin, DeleteView):

    model = Articulo
    template_name = './Articulos/Articulo_delete.html'
    success_url = '/listaArticulos/'

