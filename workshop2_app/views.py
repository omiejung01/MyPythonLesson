from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)


def movie_list(request):
    list = [{'name': x.name, 'year': x.year, 'genre': x.genre,
         }
            for x in Movie.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def movie_detail(request):
    name = request.GET.get('movie_name')
    list = [{

             'movie_name': x.name, 'year': x.year, 'genre': x.genre,
             'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
             'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
             }
            for x in Movie.objects.filter(name=name).filter(void=0).order_by('-created_time')]


    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')
