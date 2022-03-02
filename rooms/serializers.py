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
        print(beds)
        if beds < 5:
            raise serializers.ValidationError("Your house is too small")
        return beds

    def validate(self, data):
        print(data)  # OrderedDict([('name', 'posttest222')])
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")

        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")

        return data

    def update(self, instance, validated_data):
        print(instance, validated_data)  # posttest {'name': 'posttest2222'}
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.price = validated_data.get("price", instance.price)
        instance.beds = validated_data.get("beds", instance.beds)
        instance.lat = validated_data.get("lat", instance.lat)
        instance.lng = validated_data.get("lng", instance.lng)
        instance.bedrooms = validated_data.get("bedrooms", instance.bedrooms)
        instance.bathrooms = validated_data.get("bathrooms", instance.bathrooms)
        instance.check_in = validated_data.get("check_in", instance.check_in)
        instance.check_out = validated_data.get("check_out", instance.check_out)
        instance.instant_book = validated_data.get(
            "instant_book", instance.instant_book
        )
        instance.save()
        return instance


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
