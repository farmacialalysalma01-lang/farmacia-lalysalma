from django.contrib import admin
from .models import Produto, EntradaStock, SaidaStock

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "preco", "stock")
    search_fields = ("nome", "codigo")

@admin.register(EntradaStock)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "preco_compra", "data")

@admin.register(SaidaStock)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade", "preco_venda", "data")
