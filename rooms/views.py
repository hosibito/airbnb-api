from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Room as Room_models
from .serializers import RoomSerializer


@api_view(["GET"])
def list_rooms(request):
    rooms = Room_models.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)
