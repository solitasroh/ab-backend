from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # 직접 필드를 선택해야 할 때
        # fields = (
        #     "name",
        #     "kind",
        # )

        # 제외하고 싶을 때
        # exclude = ("crated_at",)

        # 모두 보여 줄 때
        fields = (
            "name",
            "kind",
        )
