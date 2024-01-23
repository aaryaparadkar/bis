from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import History
from .models import ContactUs
from .models import Goals
from .models import Services
from .models import Team
from .models import Carousel

admin.site.register(Contact)
admin.site.register(History)
admin.site.register(ContactUs)
admin.site.register(Goals)
admin.site.register(Services)
admin.site.register(Team)
admin.site.register(Carousel)
