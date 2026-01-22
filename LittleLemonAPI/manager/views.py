from django.contrib.auth.models import Group, User

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from ..models import MenuItem
from ..menu.serializer import MenuItem3Serializer


# 011626' manager group user list
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_managers( request ):
    """"""
    try:
        manager_group = Group.objects.get(name='Manager')
    except Group.DoesNotExist:
        return Response( { "detail": "Manager group not found" }, status=404 )

    users = manager_group.user_set.all().values('id', 'username', 'email')
    return Response( { "managers": list(users) } )


# 0116 POST call to '/auth/token/login'  api_view()

@api_view(['POST'])
def token_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"detail": "Username and password required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {"detail": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response({"auth_token": token.key}, status=status.HTTP_200_OK)


# --------------------------------------
# --------------------------------------

# 011726' token based authN for updating items

@api_view([ 'GET', 'PATCH' ])
@permission_classes([IsAuthenticated])
def single_item_manager( request, pk ):
    item = get_object_or_404( MenuItem, pk=pk )

    if request.method == 'GET':
        serializer = MenuItem3Serializer( item )
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = MenuItem3Serializer( item, data=request.data, partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


# --------------------------------------
# --------------------------------------

# 011726' token based authN for adding user to group delivery crew
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_to_delivery_crew(request):
    username = request.data.get("username")

    if not username:
        return Response({"detail": "username is required"}, status=400)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=404)

    try:
        group = Group.objects.get(name="Delivery crew")
    except Group.DoesNotExist:
        return Response({"detail": "Delivery crew group not found"}, status=404)

    # Add user to group
    group.user_set.add(user)

    return Response({"detail": f"{username} added to Delivery crew"})

