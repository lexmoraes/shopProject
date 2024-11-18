from django.shortcuts import render, redirect
from .models import Cliente, Produto, Venda
from .forms import ClienteForm, ProdutoForm, VendaForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def cliente_form(request, id=None):
    cliente = Cliente.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})


def funcionario_list(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'funcionarios.html', {'funcionarios': funcionarios})

def funcionario_form(request, id=None):
    funcionario = Funcionario.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=cliente)
    return render(request, 'funcionario_form.html', {'form': form})

# Similar para Produto e Venda
# Funções `produto_list`, `produto_form`, `venda_list`, `venda_form`
from django.shortcuts import render

# Create your views here.
