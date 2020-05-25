from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import Setting, UserProfile
from news.models import News, Category, Comment, Images
from user.forms import UserUpdateForm, ProfileUpdateForm
from user.models import AddNewsForm, NewsImageForm, NImages


def index(request):
    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
    category = Category.objects.all()
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'setting': setting, 'lastnews': lastnews,'profile':profile}
    return render(request,'user_profile.html',context)

def user_update(request):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your account has been update!.')
            return redirect('/user')

    else:
        setting = Setting.objects.get(pk=1)
        lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
        category = Category.objects.all()
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.userprofile)
        context = {'category': category, 'setting': setting, 'lastnews': lastnews,'user_form':user_form, 'profile_form':profile_form}
        return render(request, 'user_update.html',context)


def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was been successfully updated!.')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request,'Please correct the error below..<br>'+str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        setting = Setting.objects.get(pk=1)
        lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
        category = Category.objects.all()
        form=PasswordChangeForm(request.user)
        context = {'category': category, 'setting': setting, 'lastnews': lastnews,'form':form}
        return render(request, 'change_password.html',context)

@login_required(login_url='/login') #check login
def comments(request):
    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
    category = Category.objects.all()
    current_user=request.user
    comments=Comment.objects.filter(user_id=current_user.id).order_by('-id')
    context = {'category': category, 'setting': setting, 'lastnews': lastnews, 'comments': comments}
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login') #check login
def deletecomments(request,id):
    current_user=request.user
    Comment.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request,'Comment deleted..')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login') #check login
def mynews(request):
    setting = Setting.objects.get(pk=1)
    lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
    category = Category.objects.all()
    current_user=request.user
    news=News.objects.filter(user_id=current_user.id).order_by('-id')
    context = {'category': category, 'setting': setting, 'lastnews': lastnews, 'news': news}
    return render(request, 'user_mynews.html', context)

@login_required(login_url='/login') #check login
def deletenews(request,id):
    current_user=request.user
    News.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request,'News deleted..')
    return HttpResponseRedirect('/user/mynews')

@login_required(login_url='/login') #check login
def addnews(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST,request.FILES)
        if form.is_valid():
            current_user=request.user
            data=News()
            data.user_id=current_user.id
            data.title=form.cleaned_data['title']
            data.keywords=form.cleaned_data['keywords']
            data.description=form.cleaned_data['description']
            data.image=form.cleaned_data['image']
            data.Category=form.cleaned_data['Category']
            data.slug=form.cleaned_data['slug']
            data.detail=form.cleaned_data['detail']
            data.status=True
            data.lastNews=False
            data.save()
            messages.success(request,'Your news Instaerted successfully')
            return HttpResponseRedirect('/user/mynews')
        else:
            messages.error(request, 'News Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/user/addnews')
    else:
        setting = Setting.objects.get(pk=1)
        lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
        category = Category.objects.all()
        form = AddNewsForm()
        context = {'category': category, 'setting': setting, 'lastnews': lastnews, 'form': form}
        return render(request, 'user_addnews.html', context)

@login_required(login_url='/login') #check login
def editnews(request,id):
    news=News.objects.get(id=id)
    if request.method == 'POST':
        form = AddNewsForm(request.POST,request.FILES,instance=news)
        if form.is_valid():
            form.save()
            messages.success(request,'Your news update successfully')
            return HttpResponseRedirect('/user/mynews')
        else:
            messages.error(request, 'News Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/user/editnews'+str(id))
    else:
        setting = Setting.objects.get(pk=1)
        lastnews = News.objects.filter(lastNews='True').order_by('?')[:9]
        category = Category.objects.all()
        form = AddNewsForm(instance=news)
        context = {'category': category, 'setting': setting, 'lastnews': lastnews, 'form': form}
        return render(request, 'user_addnews.html', context)


def newsaddimage(request,id):
    if request.method == 'POST':
        lasturl=request.META.get('HTTP_REFERER')
        form = NewsImageForm(request.POST,request.FILES)
        if form.is_valid():
            data=Images()
            data.title=form.cleaned_data['title']
            data.new_id=id
            data.image=form.cleaned_data['image']
            data.save()
            messages.success(request,'Your image has been successfully uploaded')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Form Error: ' + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        news=News.objects.get(id=id)
        images=Images.objects.filter(new_id=id)
        form=NewsImageForm()
        context = {'news':news,'images':images,'form':form}
        return render(request, 'news_gallery.html', context)