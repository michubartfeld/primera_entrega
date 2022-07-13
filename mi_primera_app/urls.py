from django.urls import path
from mi_primera_app.views import (mostrar_index, comprador_formulario, stock_formulario, vendedor_formulario, formulario_busqueda)

urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('comprador/', comprador_formulario),
    path('stock/', stock_formulario),
    path('vendedor/', vendedor_formulario),
    path('buscar/', formulario_busqueda)
]