from django.shortcuts import render

from AppProyectoFinalPython.models import Articulo

# Create your views here.


def lista_articulos(self):
        
    return render(self, "lista-articulos.html")



def detalleArticulo(request, id):    
            
    articulo = Articulo.objects.get(id=id)    
    
    return render(request, "detalle-articulo.html", {"Articulo": articulo, "id": articulo.id})