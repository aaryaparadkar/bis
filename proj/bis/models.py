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
    
class Goals(models.Model):
    heading1 = models.CharField(max_length = 15)
    body1 = models.CharField(max_length = 50)
    heading2 = models.CharField(max_length = 15)
    body2 = models.CharField(max_length = 50)
    heading3 = models.CharField(max_length = 15)
    body3 = models.CharField(max_length = 50)
    def __str__(self):
        return self.heading1

class Services(models.Model):
    title = models.CharField(max_length = 20)
    heading1 = models.CharField(max_length = 15)
    content1 = models.CharField(max_length = 30)
    heading2 = models.CharField(max_length = 15)
    content2 = models.CharField(max_length = 30)
    heading3 = models.CharField(max_length = 15)
    content3 = models.CharField(max_length = 30)
    heading4 = models.CharField(max_length = 15)
    content4 = models.CharField(max_length = 30)
    def __str__(self):
        return self.title
    
class Team(models.Model):
    title = models.CharField(max_length = 20)
    name1 = models.CharField(max_length = 20)
    designation1 = models.CharField(max_length = 20)
    name2 = models.CharField(max_length = 20)
    designation2 = models.CharField(max_length = 20)
    name3 = models.CharField(max_length = 20)
    designation3 = models.CharField(max_length = 20)
    def __str__(self):
        return self.title
