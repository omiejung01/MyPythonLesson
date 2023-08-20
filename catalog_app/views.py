from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'vaar1': 'This is to handle inpput',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)