from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .models import Room as Room_models
from .serializers import RoomSerializer


class OwnPagination(PageNumberPagination):
    page_size = 20


class RoomsView(APIView):
    def get(self, request):
        paginator = OwnPagination()
        rooms = Room_models.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            # print(request.data)
            # serializer.save(user=request.user)
            room = serializer.save(user=request.user)
            room_serializer = RoomSerializer(room).data
            # return Response(status=status.HTTP_200_OK)
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            print(request.data)
            print(serializer.errors)
            # {'beds': [ErrorDetail(string='Your house is too small', code='invalid')]}
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    def get_room(self, pk):  # pk값으로 룸모델에서 조회하는건 get,put,delete 다 사용하므로
        try:
            room = Room_models.objects.get(pk=pk)
            return room
        except Room_models.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            serializer = RoomSerializer(room).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            # room 오브젝트가 instence 이다. 이게 있으면 update로 인식하게된다.
            serializer = RoomSerializer(room, data=request.data, partial=True)
            # print(serializer.is_valid(), serializer.errors) # True {}
            if serializer.is_valid():
                room = serializer.save()
                return Response(RoomSerializer(room).data)  # 200을 줘야 하는거 아닌가?
            else:
                return Response(
                    data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def room_search(request):
    paginator = OwnPagination()
    rooms = Room_models.objects.filter()
    results = paginator.paginate_queryset(rooms, request)
    serializer = RoomSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)
