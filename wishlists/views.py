from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishilistSerializer


class Wishlists(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlists.object.filter(user=request.user)
        serializer = WishilistSerializer(
            all_wishlists,
            many=True,
            context={"request": request},
        )
        return Response(serializer)

    def post(self, request):
        serializer = WishilistSerializer(data=request.data)
        if serializer.is_valid:
            wishlist = serializer.save(
                user=request.user,
            )
            serializer = WishilistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
