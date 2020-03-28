from django.db import models

# Create your models here.

class Setting(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayır'),)
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    fax = models.CharField(max_length=15,blank=True)
    email = models.CharField(max_length=50,blank=True)
    smtpserver = models.CharField(max_length=20,blank=True)
    smtpemail = models.CharField(max_length=20,blank=True)
    smtppassword = models.CharField(max_length=10,blank=True)
    smtpport = models.CharField(max_length=5,blank=True)
    icon = models.ImageField(upload_to='image/',blank=True)
    facebook = models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=50,blank=True)
    twitter = models.CharField(max_length=50,blank=True)
    youtube = models.CharField(max_length=50, blank=True)
    pinterest = models.CharField(max_length=50, blank=True)
    flickr = models.CharField(max_length=50, blank=True)
    googleplus = models.CharField(max_length=50, blank=True)
    abouts = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.TextField(blank=True)
    status=models.CharField(max_length=50,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
