from rest_framework import viewsets
from .models import Room as Room_models
from .serializers import BigRoomSerializer


class RoomViewset(viewsets.ModelViewSet):

    queryset = Room_models.objects.all()
    serializer_class = BigRoomSerializer
