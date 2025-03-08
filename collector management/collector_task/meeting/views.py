from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,os
from .models import *
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
# Create your views here.
def Home(request):
    return render(request, 'calender.html')
@csrf_exempt
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event.delete()
        return JsonResponse({"message": "Event deleted successfully."}, status=200)
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found."}, status=404)

def EventRegisterView(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        Venue = request.POST.get('Venue')
        date_time = request.POST.get('date_time')
        date_time1 = request.POST.get('date_time1')
        department = request.POST.get('department')
        coordinator_name = request.POST.get('coordinator_name')
        person = request.POST.get('person')

        Event_data_has_error = False

        if not title:
            Event_data_has_error = True
            messages.error(request, "Enter Event Name")
        if not department:
            Event_data_has_error = True
            messages.error(request, "Enter Department Name")
        if not coordinator_name:
            Event_data_has_error = True
            messages.error(request, "Enter Coordinator Name")
        if Event.objects.filter(date_time=date_time, Venue=Venue).exists():
            Event_data_has_error = True
            messages.error(request, "Event already booked on that date and time.")
        if Event_data_has_error:
            return render(request, 'input.html')
        else:
            new_event = Event.objects.create(
                title=title,
                description=description,
                Venue=Venue,
                date_time=date_time,
                date_time1=date_time1,
                department=department,
                coordinator_name=coordinator_name,
                person=person
            )
            messages.success(request, "Event created successfully Check calendar")
            return redirect('calender')

    return render(request, 'input.html')

def DataView(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start and end:
        # Parse start and end times from the GET parameters
        start_date = datetime.fromisoformat(start.replace('Z', '+00:00'))
        end_date = datetime.fromisoformat(end.replace('Z', '+00:00'))
        events = Event.objects.filter(date_time__range=(start_date, end_date))
    else:
        events = Event.objects.all()
    event_list = [
        {
            "id": event.id,
            "title": event.title,
            "start": event.date_time.isoformat(),
            "end":event.date_time1.isoformat(),
            "description": event.description,
            "venue": event.Venue,
            "department" :event.department,
            "coordinator_name":event.coordinator_name,
            "person": event.person,
        }
        for event in events
    ]
    return JsonResponse(event_list, safe=False)
@csrf_exempt
def delete_events(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_ids = data.get('event_ids', [])

        if event_ids:
            # Assuming you have an Event model
            from .models import Event
            Event.objects.filter(id__in=event_ids).delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'No event IDs provided.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def EventPageView(request):
    return render(request, 'data.html')