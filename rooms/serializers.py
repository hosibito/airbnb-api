from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Room as Room_models


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Room_models
        exclude = ("modified",)
        read_only_fields = ("user", "id", "created", "updated")

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

    def get_is_fav(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False

    def create(self, validated_data):
        request = self.context.get("request")
        room = Room_models.objects.create(**validated_data, user=request.user)
        return room
