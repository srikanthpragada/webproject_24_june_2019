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


def delete_student(request):
    id = request.GET['id']
    try:
        stud = Student.objects.get(id=id)
        stud.delete()
        return redirect("/training/studentlist")
    except Exception as ex:
        print(ex)
        return render(request, 'student_delete.html',
                      {'message': "Sorry! Could not delete student!"})


def edit_student(request):
    id = request.GET['id']
    if request.method == "GET":
        try:
            stud = Student.objects.get(id=id)
            # bind form with data from instance
            f = StudentForm(instance=stud)
            return render(request, 'student_edit.html',
                          {'form': f})
        except Exception as ex:
            print(ex)
            return render(request, 'student_edit.html',
                          {'message': "Sorry! Could not get details of student!"})
    else:  # POST
        try:
            stud = Student.objects.get(id=id)
            # bind form with data from instance
            f = StudentForm(instance=stud, data=request.POST)
            f.save()
            return redirect("/training/studentlist")
        except Exception as ex:
            print(ex)
            return render(request, 'student_edit.html',
                          {'form': f,
                           'error': "Sorry!  Could not update student!"})


def search_students(request):
    if 'sname' not in request.GET:
        return render(request, 'student_search.html')
    else:
        sname = request.GET['sname']
        students =  Student.objects.filter(fullname__contains=sname)
        return render(request, 'student_search.html',
           {'sname' : sname, 'students' : students, 'length' : len(students)})

