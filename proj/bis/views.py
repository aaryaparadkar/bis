from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404

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
    
    
    contact_info_list = ContactUs.objects.latest('id')
    history_content = History.objects.latest('id')
    goals_list = Goals.objects.latest('id')
    services_list = Services.objects.all()
    team_list = Team.objects.latest('id')
    carousel_list = Carousel.objects.latest('id')
    career_list = Career.objects.prefetch_related('requirement_set').all()

    return render(request, 'bis/index.html', {
        'history_content': history_content,
        'contact_info_list': contact_info_list,
        'goals_list': goals_list,
        'services_list': services_list,
        'team_list': team_list,
        'carousel_list': carousel_list,
        'career_list': career_list,
    })
