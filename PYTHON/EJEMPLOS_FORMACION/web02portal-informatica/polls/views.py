from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):

    from django.core.mail import send_mail
    subject = "asunto"
    message = "mensaje"
    sender = "sender"
    recipients = ['quieton@hotmail.com']
    send_mail(subject, message, sender, recipients)


    return HttpResponse("222Hello, world. You're at the polls index.")