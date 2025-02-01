from rest_framework import serializers

from core import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tamanho
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estoque
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venda
        fields = '__all__'