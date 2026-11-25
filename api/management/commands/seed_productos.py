from django.core.management.base import BaseCommand
from api.models import Producto


class Command(BaseCommand):
    help = "Carga el catálogo de productos de Aroma Café"

    def handle(self, *args, **kwargs):
        productos = [
            {
                "nombre": "Espresso Clásico",
                "categoria": "cafe",
                "precio": 6.50,
                "destacado": True,
                "descripcion": "Café concentrado de origen andino, aroma intenso y cuerpo pleno.",
                "imagen": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Cappuccino Cremoso",
                "categoria": "cafe",
                "precio": 9.90,
                "destacado": True,
                "descripcion": "Espresso con leche vaporizada y una corona de espuma sedosa.",
                "imagen": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Latte Vainilla",
                "categoria": "cafe",
                "precio": 10.50,
                "descripcion": "Café suave con leche y un toque de vainilla natural.",
                "imagen": "https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Cold Brew",
                "categoria": "cafe",
                "precio": 11.00,
                "descripcion": "Café extraído en frío por 18 horas, refrescante y con notas a chocolate.",
                "imagen": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Té Verde Sencha",
                "categoria": "te",
                "precio": 7.00,
                "destacado": True,
                "descripcion": "Té verde japonés, hierba fresca y notas cítricas.",
                "imagen": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Té Chai Especiado",
                "categoria": "te",
                "precio": 8.50,
                "descripcion": "Mezcla de especias: canela, cardamomo, jengibre y clavo.",
                "imagen": "https://images.unsplash.com/photo-1597318181409-cf64d0b5d8a2?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Matcha Latte",
                "categoria": "te",
                "precio": 12.00,
                "descripcion": "Té verde matcha ceremonial con leche cremosa.",
                "imagen": "https://images.unsplash.com/photo-1536256263959-770b48d82b0a?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Cheesecake de Maracuyá",
                "categoria": "postre",
                "precio": 13.90,
                "destacado": True,
                "descripcion": "Cheesecake horneado con coulis de maracuyá fresco.",
                "imagen": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Brownie de Cacao",
                "categoria": "postre",
                "precio": 8.90,
                "descripcion": "Brownie húmedo con cacao al 70% y nueces tostadas.",
                "imagen": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Croissant de Mantequilla",
                "categoria": "snack",
                "precio": 6.00,
                "descripcion": "Croissant hojaldrado, capas crujientes y mantequilla europea.",
                "imagen": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Muffin de Arándanos",
                "categoria": "snack",
                "precio": 7.50,
                "descripcion": "Muffin esponjoso con arándanos frescos y crumble de avena.",
                "imagen": "https://images.unsplash.com/photo-1607958996333-41aef7caefaa?auto=format&fit=crop&w=600&q=70",
            },
            {
                "nombre": "Alfajor de Café",
                "categoria": "snack",
                "precio": 5.00,
                "disponible": False,
                "descripcion": "Alfajor artesanal relleno de manjar y toque de espresso.",
                "imagen": "https://images.unsplash.com/photo-1599415124974-033eeb97c3f7?auto=format&fit=crop&w=600&q=70",
            },
        ]
        creados = 0
        for data in productos:
            _, created = Producto.objects.get_or_create(
                nombre=data["nombre"], defaults=data
            )
            if created:
                creados += 1
        self.stdout.write(self.style.SUCCESS(f"✓ {creados} productos nuevos cargados."))
