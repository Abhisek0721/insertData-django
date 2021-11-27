from django.http import request
from django.shortcuts import redirect, render
from .models import Data

# Create your views here.
def home(request):
    if(request.method == "POST"):
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        age = request.POST["age"]
        location = request.POST["location"]
        data = Data.objects.create(firstName=fname, lastName=lname, Age=age, Location=location)
        data.save()
        return redirect("/showdata")
    return render(request, "index.html")

def showdata(request):
    data = Data.objects.all()
    return render(request, "showdata.html", {'data':data})