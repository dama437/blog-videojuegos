from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    destacado = models.BooleanField(default=False)
    visitas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

    def puede_editar(self, user):
        return (
            user.is_authenticated and (
                user == self.autor or
                user.is_staff or
                user.is_superuser
            )
        )


class ImagenArticulo(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return f"Imagen de {self.articulo.titulo}"

