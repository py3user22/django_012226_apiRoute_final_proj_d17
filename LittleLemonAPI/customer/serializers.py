from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, IntegerField
from ..models import MenuItem, Category
from decimal import Decimal




class Customer_MenuItemsSerializer(ModelSerializer):
    """"""
    class Meta:
        model =  MenuItem
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    """"""
    class Meta:
        model = Category
        fields = ['id', 'title']



# ----------------------------------------------------
# ----------------------------------------------------


class MenuItem4Serializer(ModelSerializer):
    """ customer serializer edited to minimum @120 """


    price_after_tax = SerializerMethodField( method_name='calculate_tax' )

    # 0119 deserialization & validation --video

    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = [ 'id', 'title', 'price', 'price_after_tax', 'category' ]

    def calculate_tax(self, product: MenuItem):
        work = round( product.price * Decimal( 1.1 ), 2)
        return work

