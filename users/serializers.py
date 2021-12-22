from rest_framework import serializers
from .models import User as User_madels


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_madels
        fields = ("username", "superhost")
