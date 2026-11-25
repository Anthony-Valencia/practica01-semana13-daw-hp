from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import TareaViewSet

router = DefaultRouter()
router.register(r"tareas", TareaViewSet, basename="tarea")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
