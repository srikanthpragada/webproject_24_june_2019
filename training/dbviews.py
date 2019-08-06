import sqlite3
from django.shortcuts import render, redirect


def list_courses(request):
    con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
    cur = con.cursor()
    cur.execute("select * from courses")
    courses = cur.fetchall()
    con.close()
    return render(request, 'list_courses.html', {'courses': courses})


def add_course(request):
    # if no data is present, do nothing
    if 'title' not in request.GET:
        return render(request, 'add_course.html')
    else:
        # insert row into table with input provided by request.GET
        title = request.GET['title']
        duration = request.GET['duration']
        fee = request.GET['fee']
        print(title,duration,fee)
        try:
            con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
            cur = con.cursor()
            cur.execute("insert into courses(title,duration,fee) values(?,?,?)",
                    (title,duration,fee))
            con.commit()
            con.close()
            return redirect("/training/courses/")
            # return render(request, 'add_course.html',{'message': "Added course successfully!"})
        except Exception as ex:
            print("Error : " + str(ex))
            return render(request, 'add_course.html',
                          {'message' : "Sorry! Could not add course!",
                           'title' : title,
                           'duration' : duration,
                           'fee' : fee})

