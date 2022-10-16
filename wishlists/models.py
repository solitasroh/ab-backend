from django.db import models
from common.models import ModelMixin


class Wishlist(ModelMixin):
    name = models.CharField(
        max_length=150,
    )
    room = models.ManyToManyField(
        "rooms.Room",
        related_name="wishlists",
    )
    experience = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self) -> str:
        return self.name
