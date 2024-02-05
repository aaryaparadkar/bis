# admin.py
from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Contact, History, ContactUs, Goals, Services, Team, Carousel, Career, Requirement, Projects, Additional

class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2})},
    }

class CareerAdmin(admin.ModelAdmin):
    inlines = [RequirementInline]

class AdditionalInline(admin.TabularInline):
    model = Additional
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2})},
    }

class ServicesAdmin(admin.ModelAdmin):
    inlines = [AdditionalInline]  # Include the AdditionalInline for Services model



admin.site.register(Contact)
admin.site.register(History)
admin.site.register(ContactUs)
admin.site.register(Goals)
admin.site.register(Services, ServicesAdmin)  # Register ServicesAdmin instead of Services
admin.site.register(Team)
admin.site.register(Carousel)
admin.site.register(Career, CareerAdmin)
admin.site.register(Requirement)
admin.site.register(Projects)
admin.site.register(Additional)
