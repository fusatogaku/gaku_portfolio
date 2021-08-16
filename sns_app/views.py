from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import BoardModel


def Toppage(request):
    return render(request, 'sns_top.html', {})

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'sns_signup.html', {})
        except IntegrityError:
            return render(request, 'sns_signup.html', {'error':'このユーザはすでに登録されています。'})
    return render(request, 'sns_signup.html', {})
    # return redirect('signup') リダイレクトで同じページを表示させようとすると、無限ループ（ページ遷移→signupfunc→redirectでページ遷移→signupfunc...）

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sns_list')
        else:
            return render(request, 'sns_login.html', { 'content':'ログインできましぇんでした。' })
    return render(request, 'sns_login.html', { 'content':'' })

# @login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'sns_list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('sns_top')

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'sns_detail.html', {'object':object})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('sns_list')

def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readperson:
        return redirect('sns_list')
    else:
        object.read = object.read + 1
        object.readperson = object.readperson + ' ' + username
        object.save()
        return redirect('sns_list')

class BoardCreate(CreateView):
    template_name = 'sns_create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('sns_list')