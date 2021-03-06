from django.shortcuts import render, HttpResponse
from datetime import datetime
from Hello.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "Successfully Applied")
    return render(request,'index.html')

    #return HttpResponse("This is HomePage")

def about(request):
    return render(request,'orders.html')
    #return HttpResponse("This is AboutPage")

def service(request):
    if request.method == "POST":
        name= request.POST.get('name')
        Email= request.POST.get('Email')
        number= request.POST.get('number')
        message= request.POST.get('message')
        contact=Contact(name='name', Email='Email', number='number', message='message', date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contact.html')
    #return HttpResponse("This is ServicePage")



    