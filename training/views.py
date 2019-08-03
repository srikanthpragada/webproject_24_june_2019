from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):
    now = str(datetime.now())
    return render(request, 'home.html',
                   {'now': now, 'title' : 'Srikanth Technologies'})
