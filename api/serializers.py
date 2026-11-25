from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    categoria_legible = serializers.SerializerMethodField()
    disponible_legible = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = (
            "url",
            "id",
            "nombre",
            "descripcion",
            "categoria",
            "categoria_legible",
            "precio",
            "disponible",
            "disponible_legible",
            "destacado",
            "imagen",
            "creado_en",
        )
        read_only_fields = ("id", "creado_en")

    def get_categoria_legible(self, obj):
        return obj.get_categoria_display()

    def get_disponible_legible(self, obj):
        return "Disponible" if obj.disponible else "Agotado"

    def validate_nombre(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )
        return value

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a cero.")
        return value

    def validate(self, data):
        # Regla de negocio: un producto destacado debe estar disponible
        if data.get("destacado") and not data.get("disponible", True):
            raise serializers.ValidationError(
                "Un producto destacado debe estar disponible."
            )
        return data
