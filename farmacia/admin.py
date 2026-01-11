from django.contrib import admin
from .models import Produto, Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "quantidade")
    search_fields = ("nome",)


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ("id", "produto", "quantidade", "preco_unitario", "data")
    list_filter = ("data",)
    search_fields = ("produto__nome",)
