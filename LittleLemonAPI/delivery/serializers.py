from rest_framework.serializers import ModelSerializer
from ..models import Delivery


class DeliverySerializer( ModelSerializer ):

    class Meta:
        model = Delivery
        fields = 'name', 'address', 'notes'


class Delivery2Serializer( ModelSerializer ):

    class Meta:
        model = Delivery
        fields = '__all__'