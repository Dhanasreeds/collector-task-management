from django.shortcuts import redirect, render

def task_home(request):
    return render(request, 'index.html')