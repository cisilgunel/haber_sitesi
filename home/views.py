from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.forms import SearchForm
from home.models import Setting, ContactFormu, ContactFormMessage
from news.models import News, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = News.objects.all()[:8]
    lastnews = News.objects.all()[:9]
    sliderr = News.objects.all()[:5]
    haberNews = News.objects.filter(Category_id__in=[19,21,20,22]).order_by('?')[:6]
    ekonomiNews = News.objects.filter(Category_id__in=[18,23,24,31]).order_by('?')[:6]
    magazinNews = News.objects.filter(Category_id__in=[12,14,30,13]).order_by('?')[:6]
    yasamNews = News.objects.filter(Category_id__in=[25,26,27,28]).order_by('?')[:6]
    sporNews = News.objects.filter(Category_id=15).order_by('?')[:6]
    teknolojiNews = News.objects.filter(Category_id=16).order_by('?')[:6]
    popularNews = News.objects.all().order_by('?')[:4]
    seyahatNews = News.objects.filter(Category_id=29).order_by('?')[:6]
    sonhaberler = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all()
    context = {'setting': setting, 'category': category,
               'page': 'home', 'sliderdata': sliderdata,
               'sliderr': sliderr, 'lastnews': lastnews,
               'ekonomiNews': ekonomiNews, 'magazinNews': magazinNews,
               'sporNews': sporNews, 'teknolojiNews': teknolojiNews,
               'popularNews': popularNews, 'seyahatNews': seyahatNews,
               'sonhaberler': sonhaberler, 'yasamNews': yasamNews, 'haberNews': haberNews}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page': 'hakkimizda', 'lastnews': lastnews}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page': 'referanslar', 'lastnews': lastnews}
    return render(request, 'referanslar.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkur ederiz")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting, 'category': category, 'form': form, 'lastnews': lastnews}
    return render(request, 'iletisim.html', context)

def category_news(request,id,slug):
    popularNews = News.objects.all().order_by('?')[:4]
    if id == 15 or id == 16 or id == 26 or id == 27 or id == 28 or id == 29 or id == 23 or \
            id == 24 or id == 31 or id == 13 or id == 14 or id == 30 or id == 20 or id == 21 or id == 22:
        news = News.objects.filter(Category_id=id)
        sliderdata = News.objects.filter(Category_id=id).order_by('?')[:8]
        sliderr = News.objects.filter(Category_id=id).order_by('?')[:5]
    elif id == 19 :
        news = News.objects.filter(Category_id__in=[19,21,20,22]).order_by('?')
        sliderdata = News.objects.filter(Category_id__in=[19,21,20,22]).order_by('?')[:8]
        sliderr = News.objects.filter(Category_id__in=[19,21,20,22]).order_by('?')[:5]
    elif id == 12 :
        news = News.objects.filter(Category_id__in=[12, 14, 30, 13]).order_by('?')
        sliderdata = News.objects.filter(Category_id__in=[12, 14, 30, 13]).order_by('?')[:8]
        sliderr = News.objects.filter(Category_id__in=[12, 14, 30, 13]).order_by('?')[:5]
    elif id == 18 :
        news = News.objects.filter(Category_id__in=[18,23,24,31]).order_by('?')
        sliderdata = News.objects.filter(Category_id__in=[18,23,24,31]).order_by('?')[:8]
        sliderr = News.objects.filter(Category_id__in=[18,23,24,31]).order_by('?')[:5]
    elif id == 25 :
        news = News.objects.filter(Category_id__in=[25,26,27,28,29]).order_by('?')
        sliderdata = News.objects.filter(Category_id__in=[25,26,27,28,29]).order_by('?')[:8]
        sliderr = News.objects.filter(Category_id__in=[25,26,27,28,29]).order_by('?')[:5]
    lastnews = News.objects.all().order_by('-id')[:9]
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    context = {'news': news, 'category': category,
               'categorydata':categorydata,'page':'category_news',
               'sliderdata': sliderdata,'sliderr': sliderr,
               'lastnews': lastnews,'popularNews': popularNews}
    return render(request, 'news.html', context)

def new_detail(request,id,slug):
    lastnews = News.objects.all()[:9]
    popularNews = News.objects.all().order_by('?')[:4]
    comments = Comment.objects.filter(news_id=id,status='True')
    category = Category.objects.all()
    new = News.objects.get(pk=id)
    image=Images.objects.filter(new_id=id)
    related=News.objects.filter(Category_id=new.Category).order_by('?')[:3]
    context ={'new': new, 'category': category,'page':'new_detail',
               'lastnews': lastnews,'popularNews': popularNews,'image': image,'related': related, 'comments':comments}
    return render(request,'new_detail.html',context)

def news_search(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            lastnews = News.objects.all()[:9]
            popularNews = News.objects.all().order_by('?')[:4]
            category=Category.objects.all()
            query=form.cleaned_data['query']
            news=News.objects.filter(title__icontains=query)
            context={'news':news,'category':category,'lastnews': lastnews,'popularNews': popularNews,}
            return render(request,'news_search.html',context)
    return HttpResponseRedirect('/')