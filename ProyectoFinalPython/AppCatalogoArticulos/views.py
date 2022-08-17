from django.shortcuts import render

# Create your views here.


def lista_articulos(self):
        
    return render(self, "lista-articulos.html")