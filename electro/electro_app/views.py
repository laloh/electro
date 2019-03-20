from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

"""
TODO:
[x] Quitar elementos del Index que no necesitamoss
[ ] Empezar a inyectar datos Dummy.
[ ] Evaluar el tamaño de las Fotos.
[ ] Evaluar sitio donde se insertará las Fotos
"""

# Create your views here.
def index(request):
    return render(request,'electro/index.html')
    