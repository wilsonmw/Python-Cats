from django.shortcuts import render, redirect

from .models import Cat, User

# Create your views here.

def addNewCatPage(request):
    if not request.session['user']:
        return redirect('/')
    return render(request, 'loggedInCats_app/addNewCat.html')

def addNewCat(request):
    if not request.session['user']:
        return redirect('/')
    id = request.session['user']
    cat = Cat.objects.addNewCat(request.POST, id)
    return redirect('/catsPage')

def deleteCat(request):
    if not request.session['user']:
        return redirect('/')
    Cat.objects.filter(id=request.POST['id']).delete()
    return redirect('/catsPage')

def editCat(request):
    if not request.session['user']:
        return redirect('/')
    context = {
        'cat':Cat.objects.get(id=request.POST['id']),
    }
    return render(request, 'loggedInCats_app/editCat.html', context)

def edit(request):
    if not request.session['user']:
        return redirect('/')
    catChange = Cat.objects.get(id=request.POST['id'])
    catChange.name=request.POST['name']
    catChange.age=request.POST['age']
    catChange.save()
    return redirect('/catsPage')

def show(request, id):
    if not request.session['user']:
        return redirect('/')
    context = {
        'cat':Cat.objects.get(id=id)
    }  
    return render(request, 'loggedInCats_app/show.html', context)

def addLike(request):
    if not request.session['user']:
        return redirect('/')
    cat = Cat.objects.get(id=request.POST['id'])
    cat.likes = cat.likes+1
    cat.save()
    return redirect('/catsPage')

def catsPage(request):
    if not request.session['user']:
        return redirect('/')
    context = {
        'cats':Cat.objects.all().order_by('-likes'),
        'first_name': User.objects.get(id=request.session['user']).first_name,
    }
    return render(request, 'loggedInCats_app/catsPage.html', context)
