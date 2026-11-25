from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filterset_fields = ["completada"]  # ?completada=true
    search_fields = ["titulo", "descripcion"]  # ?search=texto
    ordering_fields = ["creado_en", "titulo"]  # ?ordering=-creado_en
