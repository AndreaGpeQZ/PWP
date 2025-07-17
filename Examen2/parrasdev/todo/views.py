from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import ToDo
from .forms import ToDoForm

# CRUD WEB
def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})


# --------------------------------------------------------
# LAS 7 VISTAS HTML SEPARADAS (CADA UNA CON SU FILTRO)
# --------------------------------------------------------

# 1. Lista de todos los pendientes (solo IDs)
def lista_todos_ids(request):
    pendientes = ToDo.objects.all().values_list('id', flat=True)
    return render(request, 'todo/lista_todos_ids.html', {'pendientes': pendientes})

# 2. Lista de todos los pendientes (IDs y Titles)
def lista_todos_ids_titles(request):
    pendientes = ToDo.objects.all().values('id', 'title')
    return render(request, 'todo/lista_todos_ids_titles.html', {'pendientes': pendientes})

# 3. Pendientes SIN resolver (ID y Title)
def lista_no_resueltos_ids_titles(request):
    pendientes = ToDo.objects.filter(resolved=False).values('id', 'title')
    return render(request, 'todo/lista_no_resueltos_ids_titles.html', {'pendientes': pendientes})

# 4. Pendientes RESUELTOS (ID y Title)
def lista_resueltos_ids_titles(request):
    pendientes = ToDo.objects.filter(resolved=True).values('id', 'title')
    return render(request, 'todo/lista_resueltos_ids_titles.html', {'pendientes': pendientes})

# 5. Lista de todos los pendientes (IDs y userID)
def lista_todos_ids_userid(request):
    pendientes = ToDo.objects.all().values('id', 'userID')
    return render(request, 'todo/lista_todos_ids_userid.html', {'pendientes': pendientes})

# 6. Pendientes RESUELTOS (ID y userID)
def lista_resueltos_ids_userid(request):
    pendientes = ToDo.objects.filter(resolved=True).values('id', 'userID')
    return render(request, 'todo/lista_resueltos_ids_userid.html', {'pendientes': pendientes})

# 7. Pendientes SIN resolver (ID y userID)
def lista_no_resueltos_ids_userid(request):
    pendientes = ToDo.objects.filter(resolved=False).values('id', 'userID')
    return render(request, 'todo/lista_no_resueltos_ids_userid.html', {'pendientes': pendientes})
