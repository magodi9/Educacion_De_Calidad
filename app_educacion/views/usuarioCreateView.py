from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from app_educacion.serializers.usuarioSerializer import UsuarioSerializer


class UsuarioCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"cedula":request.data["cedula"],
                    "password":request.data["password"],}
                     
        try:
    
           tokenSerializer = TokenObtainPairSerializer(data=tokenData)
           tokenSerializer.is_valid(raise_exception=True)
           return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
  
        except Exception as e:
           print(e)
           return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

