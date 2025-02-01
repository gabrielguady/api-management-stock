from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        null=False,
        db_column='id',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        db_column='date_created_at',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        db_column='date_updated_at',
    )
    active = models.BooleanField(
        default=True,
        null=False,
        db_column='cs_active',
    )

    class Meta:
        abstract = True
        managed = True


class Item(ModelBase):
    nome = models.CharField(max_length=100, unique=True)  # Nome do item (Camisa, Calça, etc.)

    class Meta:
        db_table = 'items'
        managed = True

    # def str(self):
    #     return self.nome


class Tamanho(ModelBase):
    nome = models.CharField(max_length=10, unique=True)  # Nome do tamanho (P, M, G, etc.)

    class Meta:
        managed = True
        db_column = 'tamanho'

    # def str(self):
    #     return self.nome


class Estoque(ModelBase):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Relação com o item
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)  # Relação com o tamanho
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantidade_estoque = models.IntegerField(
        null=False,
        db_column='quantidade_estoque',
        validators=[MinValueValidator(0)],
    )

    class Meta:
        unique_together = (('item', 'tamanho'),)
        managed = True
        db_table = 'estoque'

    # def str(self):
    #     return f"{self.item} - {self.tamanho} - R${self.preco} - {self.quantidade} unidades"


class Venda(ModelBase):
    cliente = models.CharField(
        max_length=50,
        null=False,
        db_column='cliente',

    )
    tipo_pagamento = models.CharField(
        max_length=50,
        null=False,
        db_column='tipo_pagamento',
    )
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE
    )
    data_venda = models.DateTimeField(
        null=False,
        db_column='data_venda',
    )
    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    quantidade_venda = models.IntegerField(
        validators=[MinValueValidator(1)]  # Quantidade mínima de 1
    )


    def save(self, *args, **kwargs):
        if not self.pk:  # Verifica se é uma nova venda
            estoque = self.estoque
            if estoque.quantidade_estoque >= self.quantidade_venda:
                estoque.quantidade_estoque -= self.quantidade_venda
                estoque.save()
                self.valor_total = self.estoque.preco * self.quantidade
            else:
                raise ValueError("Quantidade em estoque insuficiente.")
        super().save(*args, **kwargs)



    class Meta:
        managed = True
        db_table = 'venda'

#
# def str(self):
#     return f"Venda #{self.id} - {self.cliente} - {self.estoque} - {self.data_venda}"
