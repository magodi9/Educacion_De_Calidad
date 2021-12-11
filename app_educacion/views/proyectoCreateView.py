from django.http.request import RAISE_ERROR
from rest_framework import status, views
from rest_framework.response import Response

from app_educacion.serializers.proyectoSerializer   import ProyectoSerializer

class ProyectoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProyectoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

       
        return Response(serializer.data)
