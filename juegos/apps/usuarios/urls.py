from django.urls import path
from .views import (
    RegistroUsuarioView,
    LoginUsuarioView,
    LogoutUsuarioView,
    PerfilDetalleView,
    PerfilUsuarioView,
    EliminarUsuarioView,
)

app_name = 'usuarios'

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
    path('perfil/', PerfilDetalleView.as_view(), name='perfil'),
    path('perfil/editar/', PerfilUsuarioView.as_view(), name='perfil_editar'),
    path('perfil/eliminar/', EliminarUsuarioView.as_view(), name='perfil_eliminar'),
]
