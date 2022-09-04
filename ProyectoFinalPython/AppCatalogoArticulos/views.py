from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator

from AppProyectoFinalPython.models import Articulo, Avatar

# Create your views here.


def lista_articulos(request):
    avatar = Avatar()
    try:        
        avatar = Avatar.objects.get(user=request.user.id)        
    except:
        print("No hay datos")
        

    listado_articulos  = Articulo.objects.all()
    paginator     = Paginator(listado_articulos,8)
    pagina        = request.GET.get("page") or 1
    articulos     = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas       = range(1, articulos.paginator.num_pages + 1)
    contexto      = {"Articulos": articulos, "paginas":paginas, "pagina_actual":pagina_actual}
    busqueda      = request.GET.get("buscar")

    if(avatar.imagen):        
        contexto["url"] = avatar.imagen.url
        
    return render(request, "lista-articulos.html", contexto )




def detalleArticulo(request, id):  
    avatar = Avatar()
    try:        
        avatar = Avatar.objects.get(user=request.user.id)        
    except:
        print("No hay datos")

    articulo = Articulo.objects.get(id=id)    
    
    contexto = {"Articulo": articulo, "id": articulo.id}
    if(avatar.imagen):        
        contexto["url"] = avatar.imagen.url

    return render(request, "detalle-articulo.html", contexto)