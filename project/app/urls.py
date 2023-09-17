from django.urls import path
from . import views

urlpatterns = [
    path("", views.pagina_inicial, name='index'),
    path('registrar_compra/', views.registrar_compra, name='registrar_compra'),
    path('registrar_venda/', views.registrar_venda, name='registrar_venda'),
    path('lista_compras/', views.lista_compras, name='lista_compras'),
    path('lista_vendas/', views.lista_vendas, name='lista_vendas'),
    path('analise_com_periodo/', views.analise_com_periodo, name='analise_com_periodo'),
    path('deletar_compra/<int:compra_id>', views.deletar_compra, name='deletar_compra'),
    path('deletar_venda/<int:venda_id>', views.deletar_venda, name='deletar_venda'),
]