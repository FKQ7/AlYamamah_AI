from django.shortcuts import render
from .models import Event
def events_view(request):
    events = Event.objects.all()
    return render(request, 'event/event.html', {'events': events})


