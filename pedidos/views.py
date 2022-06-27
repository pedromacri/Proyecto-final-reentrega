from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from carrito.carrito import Carrito
from flask import redirect
from django.contrib import messages
from pedidos.models import Linea_pedido, Pedido

# Create your views here.


@login_required(login_url="/autenticacion/log")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carrito=Carrito(request)
    lineas_pedido=list()
    for key, value in carrito.carrito.items():
        lineas_pedido.append(Linea_pedido(

            producto_id=key, 
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido


        ))

    Linea_pedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.username,
        emailusuario=request.usermail
        )

    messages.success(request, "El pedido esta armado")

    return redirect("../tienda")