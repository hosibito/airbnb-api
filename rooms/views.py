from rest_framework.generics import ListAPIView


from .models import Room as Room_models
from .serializers import RoomSerializer


class ListRoomsView(ListAPIView):

    queryset = Room_models.objects.all()
    serializer_class = RoomSerializer


########################################################
from rest_framework.views import APIView
from rest_framework.response import Response


class _ListRoomsView(APIView):
    def get(self, request):
        rooms = Room_models.objects.all()
        serialized_rooms = RoomSerializer(rooms, many=True)
        return Response(serialized_rooms.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def list_rooms(request):
    rooms = Room_models.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)
