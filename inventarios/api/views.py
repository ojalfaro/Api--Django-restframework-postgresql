from rest_framework import viewsets
from inventarios.models import Product
from inventarios.api.serializers import ProductosSerilizers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    serializer_class = ProductosSerilizers

