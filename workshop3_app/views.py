from django.shortcuts import render
from .models import Movie,Attend
from django.http import HttpResponseRedirect, HttpResponse

import json

# Create your views here.

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)



def attend(request):
    movie_name = request.GET.get('movie_name')
    seat_number = request.GET.get('seat_number')
    show_time = request.GET.get('show_time')

    new_attend = Attend()

    # Auto Increment
    last_attend = Attend()

    for x in Attend.objects.order_by('attn_number'):
        last_account = x

    if Attend.objects.exists():
        attn = int(last_attend.attn_number.replace('ATN', ''))  # Attend Number
        attn += 1
    else:
        attn = 1

    new_attend.attn_number = 'ATN' + f"{attn:08d}"
    new_attend.movie_name = movie_name
    new_attend.seat_number= seat_number
    new_attend.show_time = show_time

    new_attend.save()

    list = [{
                'attn_number': new_attend.attn_number,
                'movie_name': new_attend.movie_name,
                'seat_number': new_attend.seat_number,
                'show_time': new_attend.show_time,
                'result': 'Success',
    }]
    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')

