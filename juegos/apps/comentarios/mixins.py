from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class ComentarioPermisoMixin(UserPassesTestMixin):
    """Mixin para permisos y redirección común de Comentarios."""

    def test_func(self):
        comentario = self.get_object()
        return (
            self.request.user == comentario.autor
            or self.request.user.is_superuser
            or self.request.user.is_staff
        )
    
    def get_success_url(self):
        return reverse_lazy(
            'blog:detalle_articulo',
            kwargs={'pk': self.object.articulo.pk}
        )
