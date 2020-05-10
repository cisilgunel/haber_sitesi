from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('update/',views.user_update,name='user_update'),
    path('password/',views.change_password,name='change_password'),
    path('comments/',views.comments,name='comments'),
    path('deletecomment/<int:id>',views.deletecomments,name='deletecomments'),
    path('mynews/',views.mynews,name='mynews'),
    path('deletenews/<int:id>',views.deletenews,name='deletenews'),
    #path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]
