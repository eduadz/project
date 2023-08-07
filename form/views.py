from django.shortcuts import render
from django.http import HttpResponse
from .forms import formularioCadastro

# Create your views here.
def home(request):
    form = formularioCadastro()
    return render(request,'index.html', context={
        'form': form,
    })

def processa_formulario(request):
    form = formularioCadastro(request.POST)
    if form.is_valid():
        #nome = form.data['nome']
        #email = form.data['email']
        form.save()
        return HttpResponse("Salvo com sucesso")
    return HttpResponse("Dados inválidos")