from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from news.models import Category, News, Images, Comment


class NewsImageInline(admin.TabularInline):
    model=Images
    extra=3

class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','Category','image_tag','status']
    readonly_fields = ('image_tag',)
    list_filter = ['status','Category']
    inlines = [NewsImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','new','image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ('tree_actions','indented_title',
                    'related_news_count','related_news_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(qs,News,'Category','news_cumulative_count',cumulative=True)

        qs = Category.objects.add_related_count(qs,News,'Category','news_count',cumulative=False)
        return qs

    def related_news_count(self,instance):
        return instance.news_count
    related_news_count.short_description = 'Related news (for this specific category'

    def related_news_cumulative_count(self,instance):
        return instance.news_cumulative_count
    related_news_cumulative_count.short_description = 'Related news (in tree)'
    list_filter = ['status']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'news', 'user', 'status']
    list_filter = ['status']

admin.site.register(Category,CategoryAdmin2)
admin.site.register(News,NewsAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)
