from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Medicamento(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField(default=5)

    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    data_validade = models.DateField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
