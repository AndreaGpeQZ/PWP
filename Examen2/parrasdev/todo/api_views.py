from django.http import JsonResponse
from .models import ToDo

def ids_list(request):
    data = list(ToDo.objects.values_list('id', flat=True))
    return JsonResponse(data, safe=False)

def ids_titles_list(request):
    data = list(ToDo.objects.values('id', 'title'))
    return JsonResponse(data, safe=False)

def unresolved_titles_list(request):
    data = list(ToDo.objects.filter(resolved=False).values('id', 'title'))
    return JsonResponse(data, safe=False)

def resolved_titles_list(request):
    data = list(ToDo.objects.filter(resolved=True).values('id', 'title'))
    return JsonResponse(data, safe=False)

def ids_userid_list(request):
    data = list(ToDo.objects.values('id', 'userID'))
    return JsonResponse(data, safe=False)

def resolved_userid_list(request):
    data = list(ToDo.objects.filter(resolved=True).values('id', 'userID'))
    return JsonResponse(data, safe=False)

def unresolved_userid_list(request):
    data = list(ToDo.objects.filter(resolved=False).values('id', 'userID'))
    return JsonResponse(data, safe=False)
