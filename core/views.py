from django.shortcuts import render, redirect
from .models import Cliente, Produto, Venda, Vendedor
from .forms import ClienteForm, ProdutoForm, VendaForm, VendedoresForm


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



def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def produto_form(request, id=None):
    produto = Produto.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})



def vendedor_list(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedores.html', {'vendedores': vendedores})

def vendedor_form(request, id=None):
    vendedor = Vendedor.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = VendedoresForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = VendedoresForm(instance=vendedor)
    return render(request, 'vendedor_form.html', {'form': form})

