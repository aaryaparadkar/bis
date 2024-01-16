


from django.contrib import admin
from django.urls import path
from bis.views import index

app_name = 'bis'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]