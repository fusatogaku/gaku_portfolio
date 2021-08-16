from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Todomodel
from django.urls import reverse_lazy

def Toppageview(request):
    return HttpResponse('<p1>TOP PAGE</p1>')

class Todolist(ListView):
    template_name = 'todo_list.html'
    model = Todomodel

class TodoDetail(DetailView):
    template_name = 'todo_detail.html'
    model = Todomodel

class TodoCreate(CreateView):
    template_name = 'todo_create.html'
    model = Todomodel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo_list')

class TodoDelete(DeleteView):
    template_name = 'todo_delete.html'
    model = Todomodel
    success_url = reverse_lazy('todo_list')

class TodoUpdate(UpdateView):
    template_name = 'todo_update.html'
    model = Todomodel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('todo_list')