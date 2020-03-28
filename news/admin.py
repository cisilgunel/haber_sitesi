from django.contrib import admin

# Register your models here.
from news.models import Category, News, Images

class NewsImageInline(admin.TabularInline):
    model=Images
    extra=3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status','image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','Category','image_tag','status']
    readonly_fields = ('image_tag',)
    list_filter = ['status','Category']
    inlines = [NewsImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','new','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Images,ImagesAdmin)
