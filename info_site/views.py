from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import e_form,UserForm

def register_list(request):
    if (request.method == "GET"):
        form = e_form()
        return render(request,"info_site/index.html",{'form':form})
    else:
        form = e_form(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            return HttpResponse("Your response has been recorded")

def show_list(request):
    return render(request,"info_site/redirect.html",{'employees':Employee.objects.all()}) 

def show_individual(request,pk):
    return render(request,"info_site/individual.html",{'record':Employee.objects.get(pk=pk)})

# def show_pk(request):
#     return render(request,"info_site/all.html",{'primary':Employee.objects.all()})

def login(request):
    if (request.method == "GET"):
        form = UserForm()
        return render(request, 'info_site/magic.html', {'form': form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            return render(request,"info_site/all.html",{'primary':Employee.objects.all()})
        else:
            return HttpResponse("Invalid Credentials Please contact the admin for the correct credentials")