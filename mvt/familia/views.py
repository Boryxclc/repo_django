from django.http import HttpResponse
from django.shortcuts import render
from familia.models import familia
from datetime import datetime
# Create your views here.
def inicio(request):
    return render(request, "index.html")

def lista_familia(request):
    f = familia.objects.all()
    datos = {'datos':f }
    return render( request,"lista_familia.html", datos)

def altaf(request):
    familiar = familia(firts_name="boris", last_name="de la cruz", date_birth= "1980-03-30",)
    familiar.save()
    familiar = familia(firts_name="lidice", last_name="marinovih", date_birth= "1984-11-22",)
    familiar.save()
    familiar = familia(firts_name="camilo", last_name="de la cruz", date_birth= "1983-06-21",)
    familiar.save()

    return HttpResponse("todo correcto") 
