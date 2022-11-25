from django.urls import path
from .views import Wishlists

uarlpatterns = [
    path("", Wishlists.as_view()),
]
