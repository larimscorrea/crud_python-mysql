from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PersonForm
from app.models import Person
from django.contrib import messages


# Create your views here.

def home(request):
    data = {}
    data['db'] = Person.objects.all()
    return render(request, 'index.html')

def form(request): 
    data = {}
    data['form'] = PersonForm()
    return render(request, 'form.html', data)

def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro adicionado com sucesso')
            ## return redirect('home')
            print("Registro adicionado com sucesso!")
        ## return render(request, 'form.html', {'form': PersonForm()})
            
        print("Erro ao adicionar registro:", form.errors)  # Adicione esta linha para depuração
        return HttpResponse("Erro ao adicionar o registro.")
## def view(request, pk):
##    data = {}
##    data['db'] = Person.objects.get(pk=pk)
##    return render(request, 'view.html') 