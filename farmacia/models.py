from django.db import models


class Medicamento(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    fornecedor = models.CharField(max_length=120, blank=True, null=True)

    quantidade = models.IntegerField(default=0)

    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    data_validade = models.DateField(blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda de {self.medicamento.nome}"
