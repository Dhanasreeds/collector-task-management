from django.shortcuts import redirect, render

def dashboard(request):
    return render(request, 'index.html')

def announcement_redirect(request):
    return redirect('/announcement/')

def task_tracker_redirect(request):
    return redirect('/task-tracker/')

def ai_prediction_redirect(request):
    return redirect('/ai-prediction/')

def ai_documentation_redirect(request):
    return redirect('/ai-documentation/')

def meeting_scheduler_redirect(request):
    return redirect('/meeting-scheduler/')

def logout_view(request):
    return redirect('/login/')
