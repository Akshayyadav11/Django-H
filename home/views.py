from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    # return HttpResponse('This is home page')
    context={
        'variable':'this is sent'
    }
    return render(request, 'index.html', context)
def about(request):
    # return HttpResponse('This is about page')
    return render(request, 'about.html')
def services(request):
    # return HttpResponse('This is services page')
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse('This is contact page')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        phone = request.POST.get('phone')
        contact = Contact(name = name, email = email, phone=phone, description=desc)
        contact.save()
    return render(request, 'contact.html')