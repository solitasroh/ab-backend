from django.db import models

# Create your models here.
from common.models import ModelMixin


class Category(ModelMixin):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
