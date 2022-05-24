from django.shortcuts import render
from familia.models import familia
# Create your views here.
def inicio(request):
    return render(request, "index.html")

def lista_familia(request):
    f = familia.objects.all()
    pass
