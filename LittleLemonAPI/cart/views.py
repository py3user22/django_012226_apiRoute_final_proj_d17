from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..cart.cart import Cart
from ..models import MenuItem



@api_view(['POST'])
def add_to_cart(request):
    cart = Cart(request)
    item_id = request.data.get("item_id")
    quantity = int(request.data.get("quantity", 1))

    item = MenuItem.objects.get(id=item_id)
    cart.add(item, quantity)

    return Response({"message": "Item added", "cart_count": cart.count})
