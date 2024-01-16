


from django.contrib import admin
from django.urls import path
from bis.views import index

app_name = 'bis'
urlpatterns = [
    path('', index, name='index')
]