from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def helloworldview(request):
    
    templates = "hello.html"

    methods = ["append()", "extend()", "insert()", "remove()","pop()", "clear()", "index()", "count()","sort()", "reverse()", "copy()"]

    context = {"methods": methods}    

    return render(request, templates, context)

