from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people', views.people, name= 'people'),
    path('chat', views.chat, name = 'chat'),
    path('gallery', views.gallery, name = 'gallery'),
    path('board', views.board, name = 'board'),
    path('register', views.UserFormView.as_view(), name='register'),
    path('add_profile', views.add_profile, name = 'add_profile'),
    path('post', views.post, name="post"),
    path('messages',views.messages, name = 'messages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)