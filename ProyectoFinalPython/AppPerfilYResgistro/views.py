from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from AppPerfilYResgistro.forms import UsuarioRegistroForm

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
