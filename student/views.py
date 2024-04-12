from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentForm
from .models import Students

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sanju (request):
    return HttpResponse("Hello sanju")


def mypage(request):
    return render(request,'sanju.html')

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('index')
            form = StudentForm()
    else:
        form = StudentForm()
    stud = Students.objects.all()
    return render(request, 'create.html', {'form': form, 'stud': stud})


def update_data(request, id):
    if request.method == 'POST':
        pi = Students.objects.get(pk=id)
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Students.objects.get(pk=id)
        fm = StudentForm(instance=pi)
    return render(request, 'update.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = Students.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

