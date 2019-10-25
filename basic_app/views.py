from django.shortcuts import render
from django.http import  HttpResponseRedirect
# from django.views import View
from .models import Student
from .forms import StudentForm

def index(request):
    print('here----')
    print(request.method)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    all_students = Student.objects.all()
    my_dict = {'output': 'Hello I am from views.py', 'form':form, 'students': all_students}
    return render(request, 'basic_app/index.html', context=my_dict)