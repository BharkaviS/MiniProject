from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def home(request):
    template = 'SendMail/home.html'
    context = {"home":home}
    return render(request,template,context)

def leave(request):
    template ="SendMail/leave.html"
    return render(request,template)


def email(request):
    subject = 'Testing-Application for leave'
    message = 'Mr.xyz wants to take a leave tomorrow.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ucs17114@rmd.ac.in','sashibharkavi@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('<h1>Leave application sent!</h1>')
