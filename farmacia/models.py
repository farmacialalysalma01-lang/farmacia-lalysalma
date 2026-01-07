from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    fornecedor = models.CharField(max_length=150, blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
