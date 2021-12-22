from rest_framework import serializers

from users.serializers import TinyUserSerializer
from .models import Room as Room_models


class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Room_models
        fields = ("name", "price", "instant_book", "user")


#########################################################
class _RoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    instant_book = serializers.BooleanField()
