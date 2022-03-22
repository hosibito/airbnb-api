from rest_framework import serializers
from .models import User as User_madels


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_madels
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "superhost",
        )


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_madels
        # fields = ("username", "superhost")  # 표시할것을 명기
        exclude = (  # 뺄것을 명기
            "is_staff",
            "is_active",
            "favs",
            "date_joined",
        )


class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_madels
        fields = ("username", "first_name", "last_name", "email")

    def validate_first_name(self, value):
        print(value)
        return value.upper()
