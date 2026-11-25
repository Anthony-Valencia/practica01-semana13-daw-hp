from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.HyperlinkedModelSerializer):
    # Campo calculado de solo lectura
    estado_legible = serializers.SerializerMethodField()

    class Meta:
        model = Tarea
        fields = (
            "url",
            "id",
            "titulo",
            "descripcion",
            "completada",
            "estado_legible",
            "creado_en",
        )
        read_only_fields = ("id", "creado_en")

    def get_estado_legible(self, obj):
        return "Completada" if obj.completada else "Pendiente"

    def validate_titulo(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "El título debe tener al menos 3 caracteres."
            )
        return value.strip()

    def validate(self, data):
        # Validación cruzada a nivel de objeto (ejemplo didáctico)
        if data.get("completada") and not data.get("descripcion"):
            raise serializers.ValidationError(
                "Una tarea completada debe tener una descripción."
            )
        return data
