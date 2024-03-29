"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('home/',include('home.urls')),
    path('news/',include('news.urls')),
    path('user/',include('user.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('kunye/', views.kunye, name='kunye'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('reklamver/', views.reklamver, name='reklamver'),
    path('faq/', views.faq, name='faq'),
    path('category/<int:id>/<slug:slug>/',views.category_news, name='category_news'),
    path('new/<int:id>/<slug:slug>/',views.new_detail, name='new_detail'),
    path('search/',views.news_search, name='news_search'),
    path('search_auto/',views.news_search_auto, name='news_search_auto'),
    path('logout/',views.logout_view, name='logout_view'),
    path('login/',views.login_view, name='login_view'),
    path('signup/',views.signup_view, name='signup_view'),
]

if settings.DEBUG: #new
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
