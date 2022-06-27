from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto=Formulario_contacto()

    if request.method=="POST":
        formulario_contacto=Formulario_contacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django", 
            "El usuario con nombre {} con la direccion {} te escribe lo siguiente:\n\n {}".format(nombre, email, contenido),
            "", ["peimacri98@gmail.com"],reply_to=[email])

            try:
                email.send()
            
            except:
                redirect("/contacto/?incorrecto")

            return redirect("/contacto/?correcto")
    return render(request, 'contacto/contacto.html', {'Mi_formulario' : formulario_contacto}) 



