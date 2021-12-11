from django.db    import models

class Proyecto(models.Model):
    proyecto_id      =  models.BigAutoField(primary_key=True)
    titulo_proyecto  =  models.CharField('Titulo Proyecto' ,max_length=50)
    resumen          =  models.CharField('Resumen' , max_length=255)
    objetivos        =  models.CharField('Objetivos' , max_length=255)
    conclusiones     =  models.CharField('Conclusiones', max_length=255)
    metodologia      =  models.CharField('Metodologia', max_length=255)    
    presupuesto      =  models.IntegerField('Presupuesto')
    fecha_inicio     =  models.DateField('Fecha de Inicio' ,max_length=50)
    fecha_cierre     =  models.DateField('Fecha de Cierre' ,max_length=50)
