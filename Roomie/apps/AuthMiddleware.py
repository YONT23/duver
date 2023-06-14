"""
File in which we have the middleware for Django for Authenticating API requests
"""
import logging
from django.contrib.auth.backends import BaseBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed, TokenBackendError, TokenError
from django.core.exceptions import PermissionDenied
# Initialize logger
logger = logging.getLogger(__name__)

# Get JWT secret key

SECRET_KEY = 'secret_or_key'


def create_response(request_id, code, message):

    try:
        req = str(request_id)
        data = {"data": message, "code": int(code), "request_id": req}
        return data
    except Exception as creation_error:
        logger.error(f'create_response:{creation_error}')


class CustomMiddleware(BaseBackend):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.auth(request)
        return response

    def auth(self, request):
        try:
            
            a = ['/auth/login/', '/auth/register/','/maestra/dependencias/','/maestra/create/']
            if a.__contains__(request.path):
                return None
            auth = JWTAuthentication()
            tokenUser, token = auth.authenticate(request)
            if request.user.is_authenticated:
                user = User.objects.get(id=token['user_id'])
                if not user:
                    raise PermissionDenied()
                if tokenUser.username != user.username:
                    raise PermissionDenied()
            return None

        except jwt.ExpiredSignatureError:
            response = create_response(
                "", 4001, {"message": "Authentication token has expired"})
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=401)
        except (InvalidToken, AuthenticationFailed, TokenBackendError, TokenError):
            response = create_response(
                "", 4001, {"message": "Authorization has failed, Please send valid token."})
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=401)
        except Exception as e:
            response = create_response(
                "", 4001, {"message": e})
            raise PermissionDenied(response)