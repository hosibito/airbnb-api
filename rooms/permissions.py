from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    # api/v1/rooms/ 에 오는 권한을 설정하고 싶을때.
    # def has_permission(self, request, view):
    #     ip_addr = request.META['REMOTE_ADDR']
    #     blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
    #     return not blocked

    # api/v1/rooms/151  에 오는 권한을 설정하고 싶을때.
    def has_object_permission(self, request, view, room):

        return room.user == request.user
