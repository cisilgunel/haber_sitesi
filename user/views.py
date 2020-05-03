from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting, UserProfile
from news.models import News, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.all()[:9]
    category = Category.objects.all()
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'setting': setting, 'lastnews': lastnews,'profile':profile}
    return render(request,'user_profile.html',context)
