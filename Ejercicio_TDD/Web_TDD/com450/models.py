from django.db import models

# Create your models here.

class Calificacion(models.Model):
    ci=models.CharField(max_length=10, unique=True,verbose_name='C.I.')
    nombre=models.CharField(max_length=50, verbose_name='Nombres')
    diplomados=models.PositiveIntegerField(default=0,verbose_name='Diplomados')
    especialidades=models.PositiveIntegerField(default=0,verbose_name='Especialidades')
    maestrias=models.PositiveIntegerField(default=0,verbose_name='Maestrias')
    doctorados=models.PositiveIntegerField(default=0,verbose_name='Doctorados')
    asistencia_programas=models.PositiveIntegerField(default=0,verbose_name='Asistencias')
    antiguedad=models.PositiveIntegerField(default=0,verbose_name='Antiguedad')
    experiencia=models.PositiveIntegerField(default=0,verbose_name='Experiencia')
    docente=models.PositiveIntegerField(default=0,verbose_name='Docente')
    articulos=models.PositiveIntegerField(default=0,verbose_name='Articulos')
    observaciones=models.TextField(verbose_name='Observaciones')

    class Meta:
        db_table="calificacion"

    def __str__(self):
        return self.nombre