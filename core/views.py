from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage


def index(request):
    return render(request, 'home.html')

from django.core.mail import EmailMessage

def email(request):
    name = request.POST.get('name')
    mail = request.POST.get('mail')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    body = 'Mensagem de: %s (%s) \n'%(name, mail)
    body += 'Assunto: %s \nMensagem: %s '%(subject, message)

    subject = '[Contato] %s'%(subject)
    
    mail = EmailMessage(subject, body, 'teste.pta.citi@gmail.com', ['teste.pta.citi@gmail.com'])
    result = mail.send()

    if (result):
            return HttpResponse("success")
    return HttpResponse("error")