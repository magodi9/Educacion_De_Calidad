from app_educacion.models.proyectoModel import Proyecto
from rest_framework import serializers

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ["titulo_proyecto","resumen", "objetivos","conclusiones","metodologia","presupuesto","fecha_inicio","fecha_cierre"]

        def to_representation(self,obj):
            proyectoData = Proyecto.objects.get(proyecto_id = obj.proyecto_id)
            return {
                "titulo_proyecto" : proyectoData.titulo_proyecto,
                "resumen"         : proyectoData.resumen,
                "objetivos"       : proyectoData.objetivos,
                "conclusiones"    : proyectoData.conclusiones,
                "metodologia"     : proyectoData.metodologia
            }