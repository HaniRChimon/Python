from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    return render (request, 'index.html')

def Gen (request):
    request.session['random'] = get_random_string(length=15)
    if "number" in request.session.keys():
        request.session['number'] +=1
    else:
        request.session['number'] = 1
    return redirect('/')

def Reset (request):
    request.session['number'] = 0
    return redirect('/')

