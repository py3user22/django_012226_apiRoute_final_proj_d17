from decimal import Decimal

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, IntegerField
from ..models import MenuItem, Category


# 011626 category serializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'id', 'title' ]

# ----------------------------------------------------
# ----------------------------------------------------


class MenuItem3Serializer(ModelSerializer):
    """  """

    # stock = IntegerField(source='inventory')
    price_after_tax = SerializerMethodField( method_name='calculate_tax' )

    # 0119 deserialization & validation --video
    stock = IntegerField( source='inventory' )
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = [ 'id', 'title', 'price', 'stock', 'price_after_tax', 'category' ]

    def calculate_tax(self, product: MenuItem):
        work = round( product.price * Decimal( 1.1 ), 2)
        return work


# ----------------------------------------------------
# ----------------------------------------------------
