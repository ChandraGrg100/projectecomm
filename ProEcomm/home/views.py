from django.shortcuts import render
from django.core.mail import send_mail
from .models import *

# Create your views here.

def home(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            name,
            email,
            subject,
            message,
            ['chandragurung111111@gmai.com'],
        )
        return render(request, "contact.html", {"name": name})
        data.save()

    else:
        return render(request, "contact.html")