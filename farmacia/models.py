from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.integerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class MovimentoStock(models.Model):
    TIPO_CHOICES = (
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saída"),
    )

    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE,
        related_name="movimentos"
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # Atualiza o stock automaticamente
        if self.pk is None:  # só quando cria
            if self.tipo == "ENTRADA":
                self.medicamento.quantidade += self.quantidade
            elif self.tipo == "SAIDA":
                self.medicamento.quantidade -= self.quantidade

            self.medicamento.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo} - {self.medicamento.nome}"
