from django.db import models


class Producto(models.Model):
    CATEGORIAS = [
        ("cafe", "Café"),
        ("te", "Té"),
        ("postre", "Postre"),
        ("snack", "Snack"),
    ]

    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="cafe")
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    imagen = models.URLField(blank=True, help_text="URL de la imagen del producto")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        indexes = [
            models.Index(fields=["categoria"]),
            models.Index(fields=["disponible"]),
        ]

    def __str__(self):
        return f"{self.nombre} (S/ {self.precio})"
