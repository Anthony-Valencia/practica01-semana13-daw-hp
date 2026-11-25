from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]  # las más recientes primero
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return str(self.titulo)
