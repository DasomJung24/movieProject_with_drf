import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from megabox_clone_project.utils import get_or_none
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1 or len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            raise exceptions.AuthenticationFailed('Invalid authentication. Could not decode token.')

        pk = payload.get('user_id', None)

        user = get_or_none(User, pk=pk)

        if not user:
            raise exceptions.AuthenticationFailed('No user matching this token was found.')

        return user, token