from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people', views.people, name= 'people'),
    path('chat', views.chat, name = 'chat'),
    path('gallery', views.gallery, name = 'gallery'),
    path('register', views.UserFormView.as_view(), name='register'),
    path('add_profile', views.add_profile, name = 'add_profile'),
]