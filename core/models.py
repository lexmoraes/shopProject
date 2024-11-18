from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    matrícula = models.Charfield(unique=True, MinLengthValidator=6)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.cliente} - {self.produto} - {self.funcionario}'
