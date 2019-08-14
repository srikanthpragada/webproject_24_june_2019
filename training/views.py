from django.shortcuts import render
from datetime import datetime
from .forms import AddForm
from django.http import HttpResponse


# Create your views here.

def home(request):
    now = str(datetime.now())
    return render(request, 'home.html',
                  {'now': now, 'title': 'Srikanth Technologies'})


def add_numbers(request):
    if request.method == "POST":
        f = AddForm(request.POST)
        if f.is_valid():
            fn = f.cleaned_data['first']
            sn = f.cleaned_data['second']
            total = fn + sn
            return render(request, 'add_numbers.html',
                          {'form': f, 'total': total})
    else:  # GET
        f = AddForm()

    return render(request, 'add_numbers.html',
                  {'form': f})


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def ajax_now(request):
    return HttpResponse(str(datetime.now()))
