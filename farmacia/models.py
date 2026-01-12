from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome


class EntradaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrada - {self.produto.nome} ({self.quantidade})"


class SaidaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saída - {self.produto.nome} ({self.quantidade})"


class Venda(models.Model):
    Forma_Pagamento = [
        ("Dinheiro", "Dinheiro"),
        ("M-Pesa", "M-Pesa"),
        ("E-Mola", "E-Mola"),
        ("Cartão", "Cartão"),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=100, blank=True)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO)
    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.id} - {self.produto.nome}"
