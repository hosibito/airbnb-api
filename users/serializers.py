from rest_framework import serializers
from .models import User as User_madels


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_madels
        # fields = ("username", "superhost")  # 표시할것을 명기
        exclude = (  # 뺄것을 명기
            "groups",
            "user_permissions",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "favs",
        )
