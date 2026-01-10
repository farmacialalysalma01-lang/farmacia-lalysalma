from django.contrib import admin
from .models import Medicamento, MovimentoStock


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "quantidade")
    search_fields = ("nome",)


@admin.register(MovimentoStock)
class MovimentoStockAdmin(admin.ModelAdmin):
    list_display = ("medicamento", "tipo", "quantidade", "data")
    list_filter = ("tipo", "data")
    search_fields = ("medicamento__nome",)

from .models import Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ("id", "data", "total")
