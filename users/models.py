from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MAIL = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    avatar = models.URLField(blank=True)
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        null=True,
        blank=True,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        null=True,
        blank=True,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        null=True,
        blank=True,
    )
