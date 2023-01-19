from django.shortcuts import render

from .forms import CadastroForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    form = CadastroForm()
    context = {
        'form': form
    }
    return render(request, 'cadastrar.html', context)

def deletar(request):
    return render(request, 'deletar.html')

def atualizar(request):
    return render(request, 'atualizar.html')

def pesquisar(request):
    return render(request, 'pesquisar.html')