from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('message/new', views.messageNew),
    path('message/create', views.messageCreate),
    path('message/<int:id>/delete', views.messageDelete),
    path('message/<int:id>/comment/create', views.commentCreate),
    path('message/<int:id>/comment/delete', views.commentDelete)
    #path('message/<int:id>/show', views.messageShow),
    #path('message/<int:id>/edit', views.messageEdit),
    #path('message/<int:id>/update', views.messageUpdate),
    
]