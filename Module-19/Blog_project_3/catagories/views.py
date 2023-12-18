from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_category(request):
    # user post request koreche
    if request.method == 'POST': 
        # user er post request data 
        category_form = forms.CategoryForm(request.POST)
        # post kora data valid kina check
        if category_form.is_valid():
            # jodi valid hoi database esave korbo
            category_form.save()
            # sob thik thakle take add authore pathiye dibo
            return redirect('add_category')
    else:
        # user website e gele blank form pabo
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html',{'form':category_form})