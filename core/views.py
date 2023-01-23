from django.contrib import messages
from django.shortcuts import render

from .forms import CadastroModelForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cadastrar(request):
    if str(request.method) == 'POST':
        form = CadastroModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            #cadastro = form.save(commit=False)
            # print(f'Inscricao: {cadastro.insc_imob}')
                       
            messages.success(request, 'Salvo com sucesso')
            form = CadastroModelForm()
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


def atualizar(request):
    return render(request, 'atualizar.html')


def pesquisar(request):
    return render(request, 'pesquisar.html')
