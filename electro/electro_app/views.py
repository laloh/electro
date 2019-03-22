from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Product, Images

"""
TODO:
[x] Quitar elementos del Index que no necesitamoss
[ ] Empezar a inyectar datos Dummy.
[ ] Evaluar el tamaño de las Fotos.
[ ] Evaluar sitio donde se insertará las Fotos
"""

# Create your views here.
def index(request):
    image_list = Images.objects.all()
    image_dict = {"images":image_list}
    return render(request,'electro/index.html', context=image_dict)
