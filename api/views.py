from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["categoria", "disponible", "destacado"]
    search_fields = ["nombre", "descripcion"]
    ordering_fields = ["precio", "nombre", "creado_en"]
    ordering = ["-creado_en"]

    @action(detail=False, methods=["get"])
    def destacados(self, request):
        """GET /api/productos/destacados/ — solo productos estrella."""
        qs = self.get_queryset().filter(destacado=True, disponible=True)
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["patch"])
    def toggle_disponible(self, request, pk=None):
        """PATCH /api/productos/{id}/toggle_disponible/"""
        producto = self.get_object()
        producto.disponible = not producto.disponible
        producto.save()
        return Response(self.get_serializer(producto).data)
