from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage


def index(request):
    return render(request, 'home.html')

from django.core.mail import EmailMessage

def email(request):
    print(request)
    subject = ''
    body = ''
    body += ''

    mail = EmailMessage(subject, body, 'teste.pta.citi@gmail.com', ['teste.pta.citi@gmail.com'])
    result = mail.send()

    if (result):
            return HttpResponse("success")
    return HttpResponse("error")