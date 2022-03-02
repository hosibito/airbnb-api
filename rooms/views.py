from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from .models import Room as Room_models
from .serializers import ReadRoomSerializer, WriteRoomSerializer


class RoomsView(APIView):
    def get(self, request):
        rooms = Room_models.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.data)
            # serializer.save(user=request.user)
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            # return Response(status=status.HTTP_200_OK)
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            print(request.data)
            print(serializer.errors)
            # {'beds': [ErrorDetail(string='Your house is too small', code='invalid')]}
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    def get(self, request, pk):
        print(pk)
        try:
            room = Room_models.objects.get(pk=pk)
            serializer = ReadRoomSerializer(room).data
            return Response(serializer)
        except Room_models.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        pass

    def delete(self, request):
        pass


########################################################

from rest_framework.decorators import api_view


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


@api_view(["GET", "POST"])
def __rooms_view(request):
    if request.method == "GET":
        rooms = Room_models.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == "POST":
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.data)
            # serializer.save(user=request.user)
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            # return Response(status=status.HTTP_200_OK)
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            print(request.data)
            print(serializer.errors)
            # {'beds': [ErrorDetail(string='Your house is too small', code='invalid')]}
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class _SeeRoomView(RetrieveAPIView):

    queryset = Room_models.objects.all()
    serializer_class = ReadRoomSerializer
