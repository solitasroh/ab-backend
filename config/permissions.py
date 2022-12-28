import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TrustMeBroAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # request 아직 user는 가지고 있지 않음
        username = request.headers.get("Trust-Me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # this is ruleß
        except User.DoesNotExist:
            raise AuthenticationFailed(f"No User {username}")


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Jwt")

        if not token:
            return None
        decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithms="HS256")
        pk = decoded.get("pk")
        if not pk:
            return AuthenticationFailed("Invalid Token")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed("No User")

        return None
