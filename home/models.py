from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayır'),)
    title = models.CharField(max_length=150)
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
    icon = models.ImageField(upload_to='images/',blank=True)
    facebook = models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=50,blank=True)
    twitter = models.CharField(max_length=50,blank=True)
    youtube = models.CharField(max_length=50, blank=True)
    pinterest = models.CharField(max_length=50, blank=True)
    flickr = models.CharField(max_length=50, blank=True)
    googleplus = models.CharField(max_length=50, blank=True)
    abouts = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=50,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (('New','New'),('Read','Read'),('Closed','Closed'),)
    name = models.CharField(blank=True,max_length=20)
    email = models.CharField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True,max_length=255)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name': Textarea(attrs={'class': 'input','placeholder': 'Name & Surname', 'rows': '1'}),
            'subject': Textarea(attrs={'class': 'input','placeholder': 'Subject', 'rows': '1'}),
            'email': Textarea(attrs={'class': 'input','placeholder': 'Email Address', 'rows': '1'}),
            'message': Textarea(attrs={'class': 'input','placeholder': 'Your Massage', 'rows': '5'}),
        }


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(blank=True,max_length=20)
    address=models.CharField(blank=True,max_length=150)
    city=models.CharField(blank=True,max_length=20)
    country=models.CharField(blank=True,max_length=20)
    image=models.ImageField(blank=True,upload_to='images/users')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name+' '+self.user.last_name+ '['+self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields=['phone','address','city','country','image']