from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from AppPerfilYResgistro.forms import UsuarioRegistroForm
from AppPerfilYResgistro.forms import UserEditForm

# Create your views here.


def registro(request):

    if request.method == 'POST':

        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado'})

    else:

        form = UsuarioRegistroForm()

    return render(request, "registro.html", {"miFormulario": form})


@login_required
def editar_perfil(request):
    
    print('method:', request.method)
    print('post:', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.password = data["password1"]

            usuario.save()

            return render(request, "inicio.html", {"mensaje": "Datos actualizados con éxito..."})

    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})