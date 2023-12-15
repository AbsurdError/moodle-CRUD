from django.shortcuts import render, redirect
from .models import Person
from django.db.models import Avg, Sum, Max, Min
from .forms import AddForm

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'user/index.html', context={'people': people})


def create(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            birthDay = form.cleaned_data['birthDay']
            men, _ = Person.objects.get_or_create(name=name, surname=surname, age=age,
                                              gender=gender, birthDay=birthDay)
            return redirect('home')
        else:
            form = AddForm()
            return render(request, 'user/create.html', context={'form': form})
    else:
        form = AddForm()
        return render(request, 'user/create.html', context={'form': form})


def update(request, id):
    try:
        men = Person.objects.get(id=id)
        if request.method == 'POST':
            men.name = request.POST.get('name')
            men.surname = request.POST.get('surname')
            men.age = request.POST.get('age')
            men.gender = request.POST.get('gender')
            men.birthDay = request.POST.get('birthDay')
            men.save()
            return redirect('home')
        else:
            return render(request, 'user/update.html', context={'men': men})
    except:
        return redirect('create')


def delete(request, id):
    try:
        men = Person.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('create')




def makeMen():
    p, _ = Person.objects.get_or_create(name='Tom', surname='Temofeev', age='18', gender=True, birthDay='2011-12-12')
    p, _ = Person.objects.get_or_create(name='Tom1', surname='Texsacdmofeev', age='28', gender=True, birthDay='2016-12-02')
    p, _ = Person.objects.get_or_create(name='Tom2', surname='Temosfdfeev', age='38', gender=True, birthDay='2013-02-12')
    p, _ = Person.objects.get_or_create(name='Tom3', surname='Temsfewofeev', age='19', gender=True, birthDay='2018-12-09')
    p, _ = Person.objects.get_or_create(name='Tom4', surname='Temoerwdfgfeev', age='24', gender=True, birthDay='2005-09-12')