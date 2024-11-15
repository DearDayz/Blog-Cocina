#funciones que renderizan los html
from django.shortcuts import render




def mostrar_principal(request):
    return render(request, 'index.html')

def mostrar_entry(request):
    return render(request, 'entry.html')

def mostrar_buy(request):
    return render(request, 'buy.html')