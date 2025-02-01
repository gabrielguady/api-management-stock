from rest_framework import viewsets, permissions

from core import models, serializers

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class TamanhoViewSet(viewsets.ModelViewSet):
    queryset = models.Tamanho.objects.all()
    serializer_class = serializers.TamanhoSerializer
    permission_classes = [permissions.IsAuthenticated]

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = models.Estoque.objects.all()
    serializer_class = serializers.EstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]

class VendaViewSet(viewsets.ModelViewSet):
    queryset = models.Venda.objects.all()
    serializer_class = serializers.VendaSerializer
    permission_classes = [permissions.IsAuthenticated]
