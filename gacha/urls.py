from django.contrib import admin
from django.urls import path
from .views import Indexfunc, Resultfunc

urlpatterns = [
    path('index/', Indexfunc, name="gacha_index"),
    path('result/', Resultfunc , name="gacha_result"),
]
