from django.shortcuts import render
from .models import Product, Traveler
from .forms import RegisterForm, LoginForm

from django.http import HttpResponseRedirect, HttpResponse
import json
import bcrypt

def my_salt():
    return ('$2b$12$tUimG74HOCBiAA7sm3QX9e').encode('utf-8')

# Create your views here.
def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def product_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'id': x.product_id, 'title': x.product_title, 'price': str(x.display_price),
             'image': str(x.product_pic),
         }
            for x in Product.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def product_detail(request):
    id = request.GET.get('id')
    list = [{

             'id': x.product_id, 'title': x.product_title, 'price': str(x.display_price),
        'unit': x.product_unit, 'description': str(x.description), 'image': str(x.product_pic),
             'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
             'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
             }
            for x in Product.objects.filter(product_id=id).filter(void=0).order_by('-created_time')]


    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')


def register2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            traveler = Traveler()
            form.clean()
            traveler.fullname = form.cleaned_data['fullname'].strip()
            traveler.username = form.cleaned_data['username'].strip()
            traveler.email = form.cleaned_data['email'].strip()
            traveler.phone = form.cleaned_data['phone'].strip()

            input_password = form.cleaned_data['password'].strip()

            bytePwd = input_password.encode('utf-8')
            hash = bcrypt.hashpw(bytePwd, my_salt())

            traveler.password = hash.decode('utf-8')
            traveler.save()
            # print(post.Email)
            # print(form.Password1)

            # context = {"current_email": newuser.email,
            #           "password": newuser.password,
            #           }

            request.session['new_username'] = traveler.username
            #request.session['new_password'] = newuser.password
            #request.session['display_name'] = newuser.display_name

            context = {
                'message': 'User ' + traveler.username + ' registered',
            }

            return render(request, 'register2.html', context)
    else:

        context = {
            'message': 'Error, user xx NOT registered',
        }

    return render(request, 'register2.html', context)

def register(request):
    form = RegisterForm(request.POST)

    context = { # Clear data
        'fullname': '',
        'username': '',
        'email': '',
        'phone': '',
        'password': '',
        'gender': '',

    }
    return render(request, 'register.html', {"form": form})

def login(request):
    form = LoginForm(request.POST)

    context = { # Clear data
        'email': '',
        'password': '',

    }
    return render(request, 'login.html', {"form": form})

def login2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            traveler = Traveler()
            form.clean()
            email = form.cleaned_data['email'].strip()
            input_password = form.cleaned_data['password'].strip()

            bytePwd = input_password.encode('utf-8')
            hash = bcrypt.hashpw(bytePwd, my_salt())

            password = hash.decode('utf-8')

            #print (email)
            #print (password)

            alltravelers = Traveler.objects.filter(email=email).filter(password=password)
            if len(alltravelers) > 0:
                current_traveler = alltravelers[0]
                request.session['username'] = current_traveler.username
                #request.session['new_password'] = newuser.password
                #request.session['display_name'] = newuser.display_name

                context = {
                    'message': 'Successfully Login, welcome ' + request.session['username'],
                }

                return render(request, 'login2.html', context)
            else:

                context = {
                    'message': 'Error, Password or Email are incorrect',
                }


                return render(request, 'login2.html', context)


def app_login(request):
    email = request.GET.get('email')
    input_password = request.GET.get('password')

    bytePwd = input_password.encode('utf-8')
    hash = bcrypt.hashpw(bytePwd, my_salt())
    password = hash.decode('utf-8')

    result = [{
        'email': x.email,
    } for x in Traveler.objects.filter(email=email).filter(password=password).filter(void=0)]

    #print (email)
    print (result)
    if len(result) > 0:
        list = [{'Result':'Success','Email':email}]
    else:
        list = [{"result":"Failure", "email":"None"}]

    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')