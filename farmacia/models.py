from django.db import models
from django.contrib.auth.models import User


# =========================
# PRODUTOS
# =========================
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


# =========================
# ENTRADA DE STOCK
# =========================
class EntradaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    fornecedor = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} +{self.quantidade}"


# =========================
# SAÍDA DE STOCK
# =========================
class SaidaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    motivo = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} -{self.quantidade}"


# =========================
# VENDAS
# =========================
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    cliente = models.CharField(max_length=100, blank=True)

    forma_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("Dinheiro", "Dinheiro"),
            ("M-Pesa", "M-Pesa"),
            ("E-Mola", "E-Mola"),
            ("Cartão", "Cartão"),
        ]
    )

    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id} - {self.produto.nome}"
