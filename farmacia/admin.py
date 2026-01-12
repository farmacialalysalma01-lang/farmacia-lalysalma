from .admin_dashboard import dashboard_data
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


from django.contrib.admin import AdminSite

class AlgikAdminSite(AdminSite):
    site_header = "ALGIK – Farmácia Lalysalma"
    site_title = "ALGIK Admin"
    index_title = "Painel Executivo"

    def each_context(self, request):
        context = super().each_context(request)
        context.update(dashboard_data(request))
        return context

algik_admin = AlgikAdminSite(name="algik_admin")

