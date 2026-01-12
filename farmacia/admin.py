from django.contrib import admin
from .models import Produto, EntradaStock, SaidaStock, Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "stock")
    search_fields = ("nome",)


@admin.register(EntradaStock)
class EntradaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "data")


@admin.register(SaidaStock)
class SaidaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "data")


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ("id", "produto", "quantidade", "total", "forma_pagamento", "operador", "data")
    list_filter = ("forma_pagamento", "data")
    search_fields = ("produto__nome", "cliente")
    list_per_page = 20
