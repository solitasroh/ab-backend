from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from django.db import transaction
from .serializers import AmenitySerializer, RoomDetailSerializer, RoomListSerializer
from .models import Amenity, Room
from categories.models import Category


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(
            all_rooms,
            many=True,
            context={
                "request": request,
            },
        )
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("category is required.")
                try:
                    category = Category.objects.get(pk=category_pk)
                except Category.DoesNotExist:
                    raise ParseError("category not found.")
                if category.kind != Category.CategoryKindChoices.ROOMS:
                    raise ParseError("Cateogory is not room")
                try:
                    with transaction.atomic:
                        room = serializer.save(
                            owner=request.user,
                            category=category,
                        )
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(room)

                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity not found")

            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        return Response(
            RoomDetailSerializer(
                room,
                context={
                    "request": request,
                },
            ).data
        )

    def delete(self, request, pk):
        room = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != room.owner:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        room = self.get_object(pk)

        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != room.owner:
            raise PermissionDenied

        serializer = RoomDetailSerializer(
            room,
            request.data,
            partial=True,
        )

        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("category is required.")
            try:
                category = Category.objects.get(pk=category_pk)
            except Category.DoesNotExist:
                raise ParseError("category not found.")

            if category.kind != Category.CategoryKindChoices.ROOMS:
                raise ParseError("Cateogory is not room")
            try:
                with transaction.atomic:
                    room = serializer.save(
                        owner=request.user,
                        category=category,
                    )
                    amenities = request.data.get("amenities")
                    for amenity_pk in amenities:
                        amenity = Amenity.objects.get(pk=amenity_pk)
                        room.amenities.add(amenity)
                    serializer = RoomDetailSerializer(room)
                    return Response(serializer.data)
            except Exception:
                return ParseError("amenity not found.")
        else:
            return Response(serializer.errors)


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                AmenitySerializer(amenity).data,
            )
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            amenity,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(
                AmenitySerializer(updated_amenity).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)
