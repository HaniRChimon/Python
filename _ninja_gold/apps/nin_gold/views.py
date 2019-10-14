from django.shortcuts import render, redirect
import random

def index(request):
    if "gold" in request.session:
	    request.session["gold"] = request.session['gold']
    else:
        request.session["gold"] = 0
    return render(request, "app/index.html")

def process_money (request):
    if "message" not in request.session:
        request.session["message"] = []
    if request.POST['gold'] == 'farm':
        request.session['rand'] = random.randrange(10,20)
        request.session["gold"] += request.session["rand"]
        request.session["message"].append("Earned "+ str(request.session["rand"])+ " gold from the farm!")
    elif request.POST['gold'] =='cave':
        request.session['rand'] = random.randrange(5,11)
        request.session["gold"] += request.session["rand"]
        request.session["message"].append("Earned "+ str(request.session["rand"])+ " gold from the cave!")
    elif request.POST['gold'] =='house':
        request.session['rand'] = random.randrange(2,6)
        request.session["gold"] += request.session["rand"]
        request.session["message"].append("Earned "+ str(request.session["rand"])+ " gold from the house!")
    elif request.POST['gold'] =='casino':
        request.session['rand'] = random.randrange(0,51)
        request.session["gold"] += request.session["rand"]
        request.session["message"].append("Earned "+ str(request.session["rand"])+ " gold from the casino!")
    return redirect ('/')

def reset(request):
	request.session["gold"] = 0
	request.session["message"] = []
	return redirect ('/')


