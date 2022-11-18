from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages     #----- Printing msgs while form submission -----
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable1':"this is sent1",
        'variable2':"this is sent2"
    }
 
    return render(request, 'index.html', context)
    # return HttpResponse("This is HOME page")
    
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':        #---- If form is submitted or not -----
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Success! Your message has been sent.')
    return render(request, 'contact.html')
