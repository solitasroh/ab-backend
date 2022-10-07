from django.db import models
from common.models import ModelMixin


class Wishlist(ModelMixin):
    name = models.CharField(
        max_length=150,
    )
    room = models.ManyToManyField(
        "rooms.Room",
    )
    experience = models.ManyToManyField(
        "experiences.Experience",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name
