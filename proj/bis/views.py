from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h3>Thank you!</h3>")

    return render(request, 'bis/index.html')

def history(request):
    try:
        history_content = History.objects.latest('id')
    except ObjectDoesNotExist:
        history_content = None
    
    return render(request, 'bis/index.html', {'history_content': history_content})

def contactus(request):
    contact_info_list = ContactUs.objects.all()
    return render(request, 'bis/index.html', {'contact_info_list': contact_info_list})