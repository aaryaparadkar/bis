from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class History(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.title
    
class ContactUs(models.Model):
    tagline = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    number = models.CharField(max_length = 50)
    def __str__(self):
        return self.tagline