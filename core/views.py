from django.contrib import messages
from django.shortcuts import render

from .filters import CadastroFilter
from .forms import CadastroModelForm
from .models import Base, Cadastro


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cadastrar(request):
    if str(request.method) == 'POST':
        form = CadastroModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #cadastro = form.save(commit=False)
            #print(f'Inscricao: {cadastro.insc_imob}')      
            messages.success(request, 'Salvo com sucesso')
            form = CadastroModelForm() #limpa o formulario
        else:
            messages.error(request, 'Erro ao salvar os dados.')
    else:
        form = CadastroModelForm()

    context = {
        'form': form
    }
    return render(request, 'cadastrar.html', context)


def deletar(request):
    return render(request, 'deletar.html')


def editarCadastro(request, pk):
    context = {
        'cadastro' : Cadastro.objects.get(id = pk),       
    }
    return render(request, 'editarCadastro.html', context)


def pesquisar(request):
    template_name = 'pesquisar.html'
    object_list = Cadastro.objects.all()
    cadastro_list = CadastroFilter(request.GET, queryset=object_list)

    context = {
        'object_list' : object_list,
        'filter': cadastro_list
    }
    return render(request, template_name, context)

def visualizarDados(request):
    context = {
        'cadastros' : Cadastro.objects.all()
    }
    return render(request, 'visualizarDados.html', context)

def complementodados(request, pk):
    context = {
        'cadastro' : Cadastro.objects.get(id = pk),       
    }
    return render(request, 'complementodados.html', context) 