from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

# cookie-->
def home(request):
    response = render(request,'home.html')
    response.set_cookie('name','Dalia')
    # response.set_cookie('name','Bilkis',max_age = 60*3)
    response.set_cookie('name','Bilkis',expires=datetime.utcnow()+timedelta(days = 7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request,'del_cookie.html')
    response.delete_cookie('name')
    return response

# Session framework --> temporary work in backend
#  Cookie --> dark theme,language,remeberme etc


# Session framework -->
def set_session(request):
    # data = {
    #     'name':'Dalia',
    #     'age':'21',
    #     'language':'Bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'Dalia'
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'get_session.html',{'name':name})
    else:
        return HttpResponse('your session has been expired kindly login again')


def delete_session(request):
    # just delete name-->
    # del request.session['name']
    # to delete full-->
    request.session.flush()
    return render(request,'del_session.html')

