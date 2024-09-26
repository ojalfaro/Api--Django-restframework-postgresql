from rest_framework import serializers
from inventarios.models import Product


class ProductosSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

