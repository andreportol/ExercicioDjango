from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def deletar(request):
    return render(request, 'deletar.html')

def atualizar(request):
    return render(request, 'atualizar.html')

def pesquisar(request):
    return render(request, 'pesquisar.html')