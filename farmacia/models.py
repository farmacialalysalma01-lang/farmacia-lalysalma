from django.db import models
from django.contrib.auth.models import User


# =========================
# PRODUTO
# =========================
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome


# =========================
# ENTRADA DE STOCK
# =========================
class EntradaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrada {self.produto.nome}"


# =========================
# SAÍDA DE STOCK
# =========================
class SaidaStock(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saída {self.produto.nome}"


# =========================
# VENDA
# =========================

FORMA_PAGAMENTO = (
    ("Dinheiro", "Dinheiro"),
    ("M-Pesa", "M-Pesa"),
    ("E-Mola", "E-Mola"),
    ("Cartão", "Cartão"),
)

class Venda(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=100, blank=True)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO, default="Dinheiro")
    data = models.DateTimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Venda {self.id}"


# =========================
# ITENS DA VENDA (CARRINHO)
# =========================
class VendaItem(models.Model):
    venda = models.ForeignKey("Venda", on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}"

