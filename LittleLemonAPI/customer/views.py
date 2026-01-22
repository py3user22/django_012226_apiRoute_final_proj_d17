from ..customer.serializers import Customer_MenuItemsSerializer, CategorySerializer, MenuItem4Serializer
from ..models import MenuItem, Category
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def view1_menu(request):
    """customer view of menu item list -- READ ONLY"""
    if request.method == 'GET':
        items = MenuItem.objects.select_related( 'category' ).all()
        category_name = request.query_params.get( 'category' )
        to_price = request.query_params.get( 'to_price' )
        search = request.query_params.get( 'search' )

        # 0113 token based add edits
        ordering = request.query_params.get( 'ordering' )
        perpage = request.query_params.get( 'perpage', default=2 )
        page =request.query_params.get( 'page', default=1 )

        if ordering:
            items = items.order_by( ordering )

        if category_name:
            items = items.filter( category__title=category_name )

        if to_price:
            items = items.filter( price__lte=to_price )

        if search:
            items = items.filter( title__icontains=search )

        serialized_items = MenuItem4Serializer( items, many=True )
        return Response( serialized_items.data )


@api_view(['GET'])
def view2_single(request, pk):
    """customer view of single --menu item list -- READ ONLY"""
    item = get_object_or_404(MenuItem, pk=pk)
    serializer = MenuItem4Serializer( item )
    return Response( serializer.data )




@api_view(['GET'])
def category_view(request):
    """api view of category list"""
    item = Category.objects.all()
    serializer = CategorySerializer(item, many=True)
    return Response(serializer.data)

