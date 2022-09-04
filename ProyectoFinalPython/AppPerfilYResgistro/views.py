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
    avatar = Avatar()
    try:        
        avatar = Avatar.objects.get(user=request.user.id)        
    except:
        print("No hay datos")

    if request.method == 'POST':

        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            #return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado'})
            return redirect('/Login')


    else:

        form = UsuarioRegistroForm()

    contexto = {"miFormulario": form}

    if(avatar.imagen):        
        contexto["url"] = avatar.imagen.url

    return render(request, "registro.html", contexto)


@login_required
def editar_perfil(request):
    avatar = Avatar()
    try:        
        avatar = Avatar.objects.get(user=request.user.id)        
    except:
        print("No hay datos")
    

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

    contexto = {"miFormulario": miFormulario}

    if(avatar.imagen):        
        contexto["url"] = avatar.imagen.url

    return render(request, "editarPerfil.html", contexto)

@login_required
def agregar_avatar(request):

    avatar = Avatar()
    try:        
        avatar = Avatar.objects.get(user=request.user.id)        
    except:
        print("No hay datos")

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

            #return render(request, 'inicio.html', {"mensaje": "Avatar cargado..."})
            return redirect('/editar-avatar')


    else:

        miFormulario = AvatarFormulario()

    contexto = {"miFormulario": miFormulario}

    if(avatar.imagen):        
        contexto["url"] = avatar.imagen.url
    return render(request, "agregarAvatar.html", contexto)