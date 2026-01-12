from django.contrib import admin
from .models import Produto, Venda, EntradaStock, SaidaStock

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco_venda", "stock")
    search_fields = ("nome",)
    list_filter = ("nome",)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ("id", "produto", "quantidade", "total", "forma_pagamento", "data")
    list_filter = ("forma_pagamento", "data")
    search_fields = ("produto__nome",)

@admin.register(EntradaStock)
class EntradaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "data")

@admin.register(SaidaStock)
class SaidaStockAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "data")
