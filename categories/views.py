from django.http import JsonResponse
from django.shortcuts import render
from .models import Category

# Create your views here.
def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            "ok": True,
            "categories": all_categories,
        }
    )
