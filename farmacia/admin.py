from django.contrib import admin
from .models import Produto, Venda, ItemVenda

admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ItemVenda)
