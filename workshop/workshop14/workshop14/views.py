from django.http import HttpResponse
from django.shortcuts import render
import random


def info(request):
    return render(request, "info.html")
    
def students(request,name):
    stu = {
        "a":25,
        "b":25,
        "c":28
    }
    age = stu[name]
    return render(request, "students.html",{"name":name,"age":age})