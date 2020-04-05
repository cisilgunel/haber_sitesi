from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from news.models import News


def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata = News.objects.all()[:8]
    lastnews = News.objects.all()[:9]
    sliderr = News.objects.all()[:5]
    context={'setting': setting, 'page':'home', 'sliderdata':sliderdata,'sliderr':sliderr,'lastnews':lastnews}
    return render(request,'index.html',context)

def hakkimizda(request):
    setting=Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    context={'setting': setting, 'page':'hakkimizda','lastnews':lastnews}
    return render(request,'hakkimizda.html',context)

def referanslar(request):
    setting=Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    context={'setting': setting, 'page':'referanslar','lastnews':lastnews}
    return render(request,'referanslar.html',context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız başarı ile gönderilmiştir. Teşekkur ederiz")
            return HttpResponseRedirect('/iletisim')

    setting=Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    form=ContactFormu()
    context={'setting': setting, 'form':form,'lastnews':lastnews}
    return render(request,'iletisim.html',context)