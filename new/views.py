import email
from email import message
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact() #creating Contact object as contact

        contact.name = name #contact.name means im calling Contact classes  name
        contact.email = email
        contact.message = message
        contact.save() # saving data
        return HttpResponse('<h1> Valar Morghulis </h1>')

    return render(request,'contacts.html')