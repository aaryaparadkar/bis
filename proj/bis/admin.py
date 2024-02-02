from django.contrib import admin
from django.forms import Textarea
from django.db import models

from .models import Contact, History, ContactUs, Goals, Services, Team, Carousel, Career, Requirement

class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2})},
    }

class CareerAdmin(admin.ModelAdmin):
    inlines = [RequirementInline]

# Register your models here.
admin.site.register(Contact)
admin.site.register(History)
admin.site.register(ContactUs)
admin.site.register(Goals)
admin.site.register(Services)
admin.site.register(Team)
admin.site.register(Carousel)
admin.site.register(Career, CareerAdmin)
admin.site.register(Requirement)  # Register Requirement model separately
