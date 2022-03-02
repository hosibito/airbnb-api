from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views


app_name = "rooms"

urlpatterns = [
    path("", views.rooms_view),
    path("<int:pk>/", views.SeeRoomView.as_view()),
]


################################################

# from . import views

# urlpatterns = [
#     path("list/", views.ListRoomsView.as_view()),
#     path("<int:pk>/", views.SeeRoomView.as_view()),
# ]

# from . import viewsets
# router = DefaultRouter()
# router.register("", viewsets.RoomViewset, basename="room")

# urlpatterns = router.urls
