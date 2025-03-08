from django.shortcuts import redirect, render

def announcement_home(request):
    return render(request, 'index.html')