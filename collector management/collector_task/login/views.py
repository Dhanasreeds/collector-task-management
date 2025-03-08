from django.shortcuts import redirect, render

def login_home(request):
    return render(request, 'index.html')