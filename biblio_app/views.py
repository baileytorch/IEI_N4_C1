from django.shortcuts import render

# Create your views here.
# inicio es una vista basada en función FBV
def inicio(request):
    return render(request,'inicio.html')