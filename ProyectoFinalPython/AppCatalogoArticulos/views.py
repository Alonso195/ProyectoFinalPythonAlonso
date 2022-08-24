from django.shortcuts import render

from AppProyectoFinalPython.models import Articulo

# Create your views here.


def lista_articulos(self):
    articulos = Articulo.objects.all()
        
    return render(self, "lista-articulos.html", {"Articulos": articulos})



def detalleArticulo(request, id):    
            
    articulo = Articulo.objects.get(id=id)    
    
    return render(request, "detalle-articulo.html", {"Articulo": articulo, "id": articulo.id})