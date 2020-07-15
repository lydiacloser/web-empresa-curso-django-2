from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\n{}".format(name, email, content), #cuerpo
                "no-contestar@inbox.mailtrap.io", #email_origen
                ["lydia.lago@closerideas.com"], #email_destino
                reply_to=[email] #reply_to
            )
            try:
                #ok
                email.send()
            except:
                #ko
                return redirect(reverse('contact')+'?fail')

    return render(request, "contact/contact.html",{'form':contact_form})