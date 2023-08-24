from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect, HttpResponse
import json

# Create your views here.
def homepage(request):
    context = {
        'vaar1': 'This is to handle inpput',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def product_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'Product ID': x.product_id, 'Product Title': x.product_title, 'Price': str(x.display_price),
         }
            for x in Product.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')