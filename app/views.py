from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request): 
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)

