from app_educacion.models.usuarioModel import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cedula' ,'nombre','correo_electronico','direccion','password','departamento','municipio_de_residencia','perfil']
        
        def to_representation(self,obj):
            usuarioData = User.objects.get(cedula=obj.cedula)
            return{
                'cedula'                   : usuarioData.cedula                  ,
                'nombre'                   : usuarioData.nombre                  ,
                'correo_electronico'       : usuarioData.correo_electronico      ,
                'direccion'                : usuarioData.direccion               ,
                'password'                 : usuarioData.password                ,
                'departamento'             : usuarioData.departamento            ,
                'municipio_de_residencia'  : usuarioData.municipio_de_residencia ,
                'perfil'                   : usuarioData.perfil                  
            }