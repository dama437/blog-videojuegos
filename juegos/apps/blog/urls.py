from django.urls import path,include
from .views import (ArticuloListView, ArticuloDetailView, ArticuloCreateView, 
                    PaginaPrincipalView)


app_name = 'blog'

urlpatterns = [
    path('', PaginaPrincipalView.as_view(), name='pagina_principal'),
    path('articulos/', ArticuloListView.as_view(), name='lista_articulos'),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name='detalle_articulo'),
    path('crear/', ArticuloCreateView.as_view(), name='crear_articulo'),

]