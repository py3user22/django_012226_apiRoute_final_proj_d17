from django.contrib.auth.models import Group, User

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from ..models import MenuItem, Category
from ..menu.serializer import MenuItem3Serializer, CategorySerializer



# 011626
# 0112 filter & search video

@api_view( ["GET", "POST"] )
def menu_items( request ):
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

        serialized_items = MenuItem3Serializer( items, many=True )
        return Response( serialized_items.data )

    elif request.method == 'POST':
        serialized_items = MenuItem3Serializer( data= request.data )
        serialized_items.is_valid( raise_exception=True )
        serialized_items.save()
        return Response( serialized_items.validated_data, status.HTTP_201_CREATED )


@api_view()
def single_item( request, pk ):
    item = get_object_or_404( MenuItem, pk=pk )
    serialized_item = MenuItem3Serializer( item )
    return Response( serialized_item.data )


# ------------------------------
# ------------------------------


#0116 category api_view() create

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return Response(
            {"detail": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)

