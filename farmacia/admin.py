from django.contrib import admin
from .models import Produto, EntradaStock, SaidaStock, Venda
from .models import Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "stock")
    search_fields = ("nome",)


@admin.register(EntradaStock)
class EntradaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "data")


@admin.register(SaidaStock)
class SaidaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "data")


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "total", "forma_pagamento", "data", "operador")
    list_filter = ("forma_pagamento", "data")
