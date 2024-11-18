from django.contrib import admin
from .models import Cliente, Produto, Venda

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Funcionario)
admin.site.register(Venda)
