from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto, Venda

@login_required
def nova_venda(request):
    produtos = Produto.objects.filter(quantidade__gt=0)

    if request.method == "POST":
        produto_id = request.POST.get("produto")
        quantidade = int(request.POST.get("quantidade"))
        cliente = request.POST.get("cliente")
        forma_pagamento = request.POST.get("forma_pagamento")

        produto = Produto.objects.get(id=produto_id)

        if quantidade > produto.quantidade:
            return render(request, "nova_venda.html", {
                "produtos": produtos,
                "erro": "Stock insuficiente"
            })

        total = quantidade * produto.preco

        venda = Venda.objects.create(
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
            total=total,
            cliente=cliente,
            forma_pagamento=forma_pagamento,
            operador=request.user
        )

        produto.quantidade -= quantidade
        produto.save()

        return redirect("historico_vendas")

    return render(request, "nova_venda.html", {"produtos": produtos})
