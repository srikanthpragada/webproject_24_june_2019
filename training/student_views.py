from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from .models import Student
from .forms import StudentForm


def home(request):
    summary = Student.objects.all().aggregate(count=Count('id'),
                                              total=Sum('feepaid'))
    return render(request, 'student_home.html', {'summary': summary})


def add(request):
    if request.method == "GET":
        f = StudentForm()
        return render(request, 'student_add.html', {'form': f})
    else:  # POST
        f = StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/training/studentlist")

        return render(request, 'student_add.html', {'form': f})


def list(request):
    return render(request, 'student_list.html',
                  {'students': Student.objects.all()})
