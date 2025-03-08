from django.shortcuts import redirect, render

def prediction_home(request):
    return render(request, 'index.html')