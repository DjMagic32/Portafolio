from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactoForm


def index(request):
    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            subject= 'Ha recibido un nuevo mensaje de ' + request.POST["Nombre_y_Apellido"]
            message=request.POST["Mensaje"] + "\n" + "\n" + 'Responder al número del cliente:  ' + request.POST["Telefono"] + "\n" + "\n" +  'Email de cliente:  ' +  request.POST["Email"] 
            email_from=settings.EMAIL_HOST_USER
            recipient_list=["dukleenteam@gmail.com"]
            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'Messagesend.html', data) 

    return render(request, 'index.html', data)

def Messagesend (request):
    return render(request, 'Messagesend.html',{})