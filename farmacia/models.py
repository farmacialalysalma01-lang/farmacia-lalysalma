from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class EntradaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrada {self.produto.nome}"


class SaidaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.produto.nome}"

from django.contrib.auth.models import User

class Venda(models.Model):
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    forma_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("Dinheiro", "Dinheiro"),
            ("M-Pesa", "M-Pesa"),
            ("E-Mola", "E-Mola"),
            ("Cartão", "Cartão"),
        ],
    )
    data = models.DateTimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.total = self.quantidade * self.preco_unitario

        # baixa o stock
        self.produto.stock -= self.quantidade
        self.produto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unid"


