from django.shortcuts import redirect, render

def documentation_home(request):
    return render(request, 'index.html')