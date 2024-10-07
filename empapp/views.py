from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def result(request):
    n1=int(request.POST['salary'])
    n2=int(request.POST['insentive'])
    if 'add' in request.POST:
        total=n1+n2
    return render(request,"index.html",{'total':total})    
