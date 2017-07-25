from django.shortcuts import render, redirect

from .models import User
from ..loggedInCats_app.models import Cat
from django.contrib import messages

# Create your views here.
def index(request):
    request.session['user']=None
    return render(request, 'cats_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    print results['errors']
    for error in results['errors']:
        messages.error(request, error)
        print error
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    for error in results['loginMsg']:
        messages.error(request, error)
    if results['status']==True:
        request.session['user']=results['user'][0].id
        return redirect('/catsPage')
    else:
        return redirect('/')
