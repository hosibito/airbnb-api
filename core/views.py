from django.core import serializers
from django.http import HttpResponse
from rooms.models import Room as Room_models


def list_rooms(request):
    data = serializers.serialize("json", Room_models.objects.all())
    response = HttpResponse(content=data)
    return response
