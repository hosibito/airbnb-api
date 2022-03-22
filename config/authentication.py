import jwt
from django.conf import settings
from rest_framework import authentication
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):  # none 가 반환되면 인증실패
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")  # 헤더에 Authorization 값을 가져옴
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except (ValueError, jwt.exceptions.DecodeError, User.DoesNotExist):
            return None
