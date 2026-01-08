from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100, blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_validade = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.quantidade})"
