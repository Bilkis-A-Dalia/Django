from django.shortcuts import render

# D:\phitron\Software development\Django\Module-1\project_2\templates
def home(request):
    return render(request,'index.html')