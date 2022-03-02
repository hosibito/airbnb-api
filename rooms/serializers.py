from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Room as Room_models


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room_models
        # fields = ("pk", "name", "price", "instant_book", "user") # 표시할것을 명기
        exclude = ("modified",)  # 뺄것을 명기


#########################################################
class _RoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    instant_book = serializers.BooleanField()
