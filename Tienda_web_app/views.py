from django.shortcuts import render, HttpResponse

from carrito.carrito import Carrito


# Create your views here.

def home(request):

    carrito=Carrito(request)

    return render(request, "Tienda_web_app/home.html")






