from django.http import HttpResponse
from datetime import datetime


# Function View
def index(request):
    return HttpResponse("<h1 style='color:red'>Welcome To Django </h1>")


def hello(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name ='Guest'

    hour = datetime.now().hour
    if hour < 12:
        msg = 'Good Morning'
    elif hour < 17:
        msg = 'Good Afternoon'
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{name}, {msg}</h1>")


