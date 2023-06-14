from rest_framework.views import APIView
from ..serializers import LoginSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.contrib.auth.models import User
from ..serializers import usuarioSerializer, personaSerializer
EXP_TIME = datetime.timedelta(hours=1)


class LoginView(APIView):
    serializer_class = LoginSerializers

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request, *args, **kwargs):
        serializers = LoginSerializers(data=request.data)

        if not serializers.is_valid():
            raise InvalidToken('Token is Invalid',
                               code=status.HTTP_400_BAD_REQUEST)
        
        token = self.get_tokens_for_user(serializers.validated_data)
        
        response = Response({'token': token, 'username': serializers.data['username'], }, status=status.HTTP_200_OK)
        response.set_cookie('token',token)
        return response

class UsuarioCreate(APIView):
    queryset = User.objects.all()
    serializer_class = usuarioSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        user = request.data['username']
        persona = request.data['persona']
        personaSerializer_ = personaSerializer(data=persona)
        if personaSerializer_.is_valid():
            user['email'] = personaSerializer_.validated_data['correo']
            createUser = usuarioSerializer(data=user)
            if createUser.is_valid():
                createUser.save()
                return Response(createUser.data, status=status.HTTP_200_OK)
            return Response(createUser.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(personaSerializer_.errors, status=status.HTTP_400_BAD_REQUEST)