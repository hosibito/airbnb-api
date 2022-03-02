from rest_framework.generics import ListAPIView, RetrieveAPIView


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Room as Room_models
from .serializers import ReadRoomSerializer, WriteRoomSerializer


@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == "GET":
        rooms = Room_models.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == "POST":
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            return Response(status=status.HTTP_200_OK)
        else:
            print(request.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SeeRoomView(RetrieveAPIView):

    queryset = Room_models.objects.all()
    serializer_class = ReadRoomSerializer


########################################################
from rest_framework.views import APIView


class _ListRoomsView(APIView):
    def get(self, request):
        rooms = Room_models.objects.all()
        serialized_rooms = ReadRoomSerializer(rooms, many=True)
        return Response(serialized_rooms.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def list_rooms(request):
    rooms = Room_models.objects.all()
    serialized_rooms = ReadRoomSerializer(rooms, many=True)  # 한개가 아닌경우 many=True
    return Response(data=serialized_rooms.data)


class __ListRoomsView(ListAPIView):

    queryset = Room_models.objects.all()
    serializer_class = ReadRoomSerializer
