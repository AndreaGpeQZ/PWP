from django.urls import path
from . import views

urlpatterns = [

    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),

   
    path('pendientes/todos-ids/', views.lista_todos_ids, name='lista_todos_ids'),
    path('pendientes/todos-ids-titles/', views.lista_todos_ids_titles, name='lista_todos_ids_titles'),
    path('pendientes/no-resueltos-ids-titles/', views.lista_no_resueltos_ids_titles, name='lista_no_resueltos_ids_titles'),
    path('pendientes/resueltos-ids-titles/', views.lista_resueltos_ids_titles, name='lista_resueltos_ids_titles'),
    path('pendientes/todos-ids-userid/', views.lista_todos_ids_userid, name='lista_todos_ids_userid'),
    path('pendientes/resueltos-ids-userid/', views.lista_resueltos_ids_userid, name='lista_resueltos_ids_userid'),
    path('pendientes/no-resueltos-ids-userid/', views.lista_no_resueltos_ids_userid, name='lista_no_resueltos_ids_userid'),
]
