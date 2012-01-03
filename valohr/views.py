#from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from valohr.models import Room

def index(request):
#    return HttpResponse("Hello, world. You're at the valohr index.")
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
    rooms_list = Room.objects.all()
    return render_to_response('index.html', {'rooms_list': rooms_list})


def detail(request, room_name):
    r = get_object_or_404(Room, room_name=room_name)
    return render_to_response('room.html', {'room': r})
