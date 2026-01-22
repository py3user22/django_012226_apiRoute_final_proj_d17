from ..models import Delivery
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ..delivery.serializers import Delivery2Serializer



# 0111 delivery model view,
@api_view(["GET", "POST"])
def delivery_list( request ):
    deliveries = Delivery.objects.all()
    serials = Delivery2Serializer( deliveries, many=True )
    return Response(serials.data)


# 0119 delivery single view mode
@api_view()
def delivery_single( request, pk ):
    item = get_object_or_404(Delivery, pk=pk)
    serializer = Delivery2Serializer(item)
    return Response(serializer.data)


#----------------------------------------------
#----------------------------------------------


# 011926 delivery views only authenticated users for view& config

def is_authorized(user, role_needed):
    return user.groups.filter(name=role_needed).exists()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delivery_create(request):
    # Only managers can create deliveries
    if not is_authorized(request.user, "Manager"):
        return Response({"detail": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)

    serializer = Delivery2Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PATCH", "GET"])
@permission_classes([IsAuthenticated])
def delivery_update(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)

    # ----- GET -----
    if request.method == "GET":
        serializer = Delivery2Serializer(delivery)
        return Response(serializer.data)

    # ----- PATCH -----
    # Delivery crew restrictions
    if is_authorized(request.user, "delivery_crew"):
        allowed_fields = {"delivery_status", "notes"}
        incoming = set(request.data.keys())

        if not incoming.issubset(allowed_fields):
            return Response(
                {"detail": "Delivery crew can only update status or notes"},
                status=status.HTTP_403_FORBIDDEN
            )

    # Manager check
    elif not is_authorized(request.user, "Manager"):
        return Response({"detail": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)

    # Perform update
    serializer = Delivery2Serializer(delivery, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#----------------------------------------------------------------
#----------------------------------------------------------------


# 012026' adding a new user to delivery crew

@api_view(["POST"])
@permission_classes([IsAdminUser])   # Only managers/admins can assign crew
def assign_delivery_crew(request):
    username = request.data.get("username")

    if not username:
        return Response(
            {"error": "username is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(
            {"error": "User not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    group, created = Group.objects.get_or_create(name="delivery_crew")
    user.groups.add(group)

    return Response(
        {"message": f"{username} added to Delivery crew"},
        status=status.HTTP_200_OK
    )


#----------------------------------------------------------------
#----------------------------------------------------------------


# 012026' adding a new user to delivery crew  demo2

@api_view(["POST"])
@permission_classes([IsAdminUser])   # Only managers/admins can create crew
def create_delivery_crew(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "username and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Create the user
    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "User already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password
    )

    # Assign to Delivery crew group
    group, created = Group.objects.get_or_create(name="Delivery crew")
    user.groups.add(group)

    return Response(
        {"message": f"User '{username}' created and added to Delivery crew"},
        status=status.HTTP_201_CREATED
    )

