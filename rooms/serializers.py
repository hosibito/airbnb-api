from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Room as Room_models


class ReadRoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room_models
        exclude = ("modified",)


class WriteRoomSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    beds = serializers.IntegerField(default=1)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)

    def create(self, validated_data):
        print(validated_data)
        # {'name': 'posttest', 'address': 'wnthwnthwnthagrea', 'price': 3000, 'beds': 3,
        # 'lat': Decimal('12.000000'), 'lng': Decimal('12.000000'), 'bedrooms': 2, 'bathrooms': 2,
        # 'check_in': datetime.time(14, 0), 'check_out': datetime.time(16, 0), 'instant_book': False,
        # 'user': <SimpleLazyObject: <User: hosibito>>}
        return Room_models.objects.create(**validated_data)

    def validate_beds(self, beds):
        if beds < 5:
            raise serializers.ValidationError("Your house is too small")
        else:
            return beds

    def validate(self, data):
        check_in = data.get("check_in")
        check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")
        else:
            return data


#########################################################
class _RoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    bedrooms = serializers.IntegerField()
    instant_book = serializers.BooleanField()


class __RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room_models
        # fields = ("pk", "name", "price", "instant_book", "user") # 표시할것을 명기
        exclude = ("modified",)  # 뺄것을 명기
