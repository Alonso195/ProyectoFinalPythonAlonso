from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from AppPerfilYResgistro.forms import UsuarioRegistroForm
from AppPerfilYResgistro.forms import UserEditForm
from AppPerfilYResgistro.forms import AvatarFormulario
from AppProyectoFinalPython.models import Avatar

# Create your views here.


def registro(request):

    if request.method == 'POST':

        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            #return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado'})
            return redirect('/')


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
            #usuario.password = data["password1"]
            #user =User.objects.get(username='admin')

            usuario.set_password(data["password1"])  

            #user.save()
            usuario.save()

            #return render(request, "inicio.html", {"mensaje": "Datos actualizados con éxito..."})
            return redirect('/')

    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "editarPerfil.html", {"miFormulario": miFormulario})

def agregar_avatar(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            try:
                record = Avatar.objects.get(user_id=request.user.id)
                if record.id:
                    record.delete()
            except:
                print("No hay datos")
            
            
            avatar = Avatar(user=request.user, imagen=miFormulario.cleaned_data['imagen'])
            print(avatar.imagen)
            avatar.save()

            return render(request, 'inicio.html', {"mensaje": "Avatar cargado..."})

    else:

        miFormulario = AvatarFormulario()

    return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})