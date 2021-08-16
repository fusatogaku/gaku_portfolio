
from django.urls import path, reverse_lazy
from .views import Toppageview, Todolist, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('', Toppageview, name='todo_top'),
    path('list/', Todolist.as_view(), name='todo_list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='todo_detail'),
    path('create/', TodoCreate.as_view(), name='todo_create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='todo_delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='todo_update'),
]
