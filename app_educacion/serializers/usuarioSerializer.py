from app_educacion.models.usuarioModel import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['cedula' ,'nombre','correo_electronico','direccion','password','departamento','municipio_de_residencia','perfil']
        
        def to_representation(self,obj):
            usuarioData = Usuario.objects.get(cedula=obj.cedula)
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