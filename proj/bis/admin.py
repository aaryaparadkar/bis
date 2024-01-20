from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import History
from .models import ContactUs

admin.site.register(Contact)
admin.site.register(History)
admin.site.register(ContactUs)