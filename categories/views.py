from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category

# Create your views here.
@api_view()
def categories(request):
    all_categories = Category.objects.all()
    return Response(
        {
            "ok": True,
            "categories": all_categories,
        }
    )
