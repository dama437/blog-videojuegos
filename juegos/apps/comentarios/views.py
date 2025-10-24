from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comentario
from .forms import ComentarioForm
from apps.blog.models import Articulo
from .mixins import comentarioPermisoMixin



class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.articulo = get_object_or_404(
            Articulo, pk=self.kwargs['articulo_id']
        )
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(
            'blog:detalle_articulo',
            kwargs={'pk': self.kwargs['articulo_id']}
        )
    
    #evitar acceso directo via GET
    def get(self, request, *args, **kwargs):
        return redirect('blog:detalle_articulo', pk=self.kwargs['articulo_id'])
    
class ComentarioUpdateView(LoginRequiredMixin, comentarioPermisoMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentarios/editar_comentario.html'

class ComentarioDeleteView(LoginRequiredMixin, comentarioPermisoMixin, DeleteView):
    model = Comentario
    template_name = 'comentarios/eliminar_comentario.html'


