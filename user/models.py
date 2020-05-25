from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.forms import ModelForm, Select, TextInput, FileInput
from django.utils.safestring import mark_safe

from news.models import News

class AddNewsForm(ModelForm):
    class Meta:
        model = News
        fields=['Category','title','slug','keywords','description','image','detail']
        widgets={
            'Category':Select(attrs={'class':'input','placeholder':'cetgory'}),
            'title':TextInput(attrs={'class':'input','placeholder':'title','size':'110'}),
            'slug':TextInput(attrs={'class':'input','placeholder':'slug','size':'110'}),
            'keywords':TextInput(attrs={'class':'input','placeholder':'keywords','size':'110'}),
            'description':TextInput(attrs={'class':'input','placeholder':'description','size':'110'}),
            'image':FileInput(attrs={'class':'input','placeholder':'image'}),
            'detail':CKEditorWidget(),
        }

class NImages(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description='Image'

class NewsImageForm(ModelForm):
    class Meta:
        model =NImages
        fields=['title','image']