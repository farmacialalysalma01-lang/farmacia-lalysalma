from django.contrib import admin
from .models import Medicamento, MovimentoStock


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "quantidade", "data_criacao")
    search_fields = ("nome",)


@admin.register(MovimentoStock)
class MovimentoStockAdmin(admin.ModelAdmin):
    list_display = ("medicamento", "tipo", "quantidade", "data")
    list_filter = ("tipo", "data")
    search_fields = ("medicamento__nome",)
