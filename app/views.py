from django.shortcuts import render
# Create your views here.

def home(request):
    data = {}
    data['carro'] = 'Fiat Uno'
    return render(request, 'index.html', data)