from django.conf                                 import settings
from django.contrib.auth.models import User
from rest_framework                              import generics, status
from rest_framework.response                     import Response
from rest_framework.permissions                  import IsAuthenticated
from rest_framework_simplejwt.backends           import TokenBackend
from app_educacion.models.usuarioModel           import User
from app_educacion.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UsuarioSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['cedula'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)