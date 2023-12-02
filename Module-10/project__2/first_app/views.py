from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d ={ 'author':'dalia','age' :15,'list':['dalia','is','best'],'birthday': datetime.datetime.now(),
        'val':' ', 'courses':[
        {
        'id':1,
        'name': 'python',
        'fee': 4000
        },
        {
        'id':2,
        'name': 'BCOM',
        'fee': 4600
        },
        {
        'id':3,
        'name': 'DLD',
        'fee': 400
        },
    ]}
    return render(request,'home.html',d)