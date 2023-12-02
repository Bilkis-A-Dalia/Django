from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d={
        'name': ['Bilkis','Akter','Dalia'],
        'date': datetime.datetime(2002,3,5),
        'default': '',
        'num': 10,
        'cap':'django',
        'cut': 'Django is fun',
        'myName':[
            {'name': 'Bilkis','age':21},
            {'name': 'Joe', 'age': 31},
            {'name': 'Josh', 'age': 19},
            ],
        'esc':'This should be fun!',
        'val':['China', 'India', 'Thailand'],
        'me':'dalia',
        'time':datetime.datetime.now(),
        'num_messages': 100,
        'value': 100,
        'var': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
    }
    return render(request,'home.html',d)