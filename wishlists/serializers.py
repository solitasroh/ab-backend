from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from wishlists.models import Wishlist


class WishilistSerializer(ModelSerializer):
    rooms = RoomListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wishlist
        fields = (
            "name",
            "rooms",
            "experiences",
        )
