from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class ComnetarioPermisoMixin(UserPassesTestMixin):
    """Mixin para permisos y redireccion comun de Comentarios."""

    def test_func(self):
        comentario = self.get_comentario.autor
        return(
            self.request.user == comentario.autor
            or self.request.user.is_superuser
            or self.request.user.is_staff
        )
    
    def get_success_url(self):
        return reverse_lazy(
            'blog:detalle_articulo',
            kwargs={'self.object.articulo.pk'}
        )