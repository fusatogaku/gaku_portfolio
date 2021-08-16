from django.contrib import admin
from django.urls import path, include
from .views import Toppage, signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate

urlpatterns = [
    path('', Toppage,),
    path('top/', Toppage, name='sns_top'),
    path('signup/', signupfunc, name='sns_signup'),
    path('login/', loginfunc, name='sns_login'),
    path('list/', listfunc, name='sns_list'),
    path('logout/', logoutfunc, name='sns_logout'),
    path('detail/<int:pk>', detailfunc, name='sns_detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='sns_create'),
]
