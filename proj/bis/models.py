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
    body1 = models.CharField(max_length = 500)
    heading2 = models.CharField(max_length = 15)
    body2 = models.CharField(max_length = 500)
    heading3 = models.CharField(max_length = 30)
    body3 = models.CharField(max_length = 500)
    def __str__(self):
        return self.heading1

    
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

class Carousel(models.Model):
    title = models.CharField(max_length = 20)
    compname1 = models.CharField(max_length = 20)
    compcontent1 = models.CharField(max_length = 400)
    compname2 = models.CharField(max_length = 20)
    compcontent2 = models.CharField(max_length = 400)
    compname3 = models.CharField(default='hui', max_length = 20)
    compcontent3 = models.CharField(default='hui', max_length = 400)
    compname4 = models.CharField(default='hui', max_length = 20)
    compcontent4 = models.CharField(default='hui', max_length = 400)
    compname5 = models.CharField(default='hui', max_length = 20)
    compcontent5 = models.CharField(default='hui', max_length = 400)
    def __str__(self):
        return self.title

class Career(models.Model):
    title = models.CharField(max_length = 20)
    position = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
    
class Requirement(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.description
    
class Projects(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='static/bis/images/5856.jpg' , upload_to='images/')
    tagline = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    def __str__(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=20)
    heading = models.CharField(max_length=500)
    content = models.CharField(max_length=500)
    additional_text = models.TextField(blank=True)  # New field for additional text
    image = models.ImageField(default='static/bis/images/5856.jpg', upload_to='images/')
    def __str__(self):
        return self.title

class Additional(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='additional_entries', default='0')
    content = models.TextField()
    def __str__(self):
        return self.content

