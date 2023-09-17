from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import Compra, Venda
# Create your views here.

def pagina_inicial(request):
    compras = Compra.objects.all().count()
    vendas = Venda.objects.all().count()
    context = {
        'compras': compras,
        'vendas': vendas
    }
    return render(request, 'pagina_inicial.html', context)

def registrar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')  # Redirecionar para a página de lista de compras após o registro
    else:
        form = CompraForm()
    
    return render(request, 'registrar_compra.html', {'form': form})

def registrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')  # Redirecionar para a página de lista de vendas após o registro
    else:
        form = VendaForm()
    
    return render(request, 'registrar_venda.html', {'form': form})

def lista_compras(request):
    compras = Compra.objects.all()  # Recupere todas as compras do banco de dados

    return render(request, 'lista_compras.html', {'compras': compras})

def lista_vendas(request):
    vendas = Venda.objects.all()  # Recupere todas as vendas do banco de dados

    return render(request, 'lista_vendas.html', {'vendas': vendas})
  
def analise_com_periodo(request):
    if request.method == 'POST':
        form = PeriodoForm(request.POST)
        if form.is_valid():
            periodo_inicio = form.cleaned_data['periodo_inicio']
            periodo_fim = form.cleaned_data['periodo_fim']

            # Realize a análise com base nas datas do período
            compras = Compra.objects.filter(data_compra__range=(periodo_inicio, periodo_fim))
            gasto_total = sum(compra.preco for compra in compras)
            vendas = Venda.objects.filter(data_venda__range=(periodo_inicio, periodo_fim))
            faturamento_total = sum(venda.preco_total for venda in vendas)
            lucro = faturamento_total - gasto_total

            return render(request, 'analise_com_periodo.html', {
                'form': form,
                'periodo_inicio': periodo_inicio,
                'periodo_fim': periodo_fim,
                'gasto_total': gasto_total,
                'faturamento_total': faturamento_total,
                'lucro': lucro,
            })
    else:
        form = PeriodoForm()

    return render(request, 'analise_com_periodo.html', {'form': form})

def deletar_compra(request, compra_id):
    compra = get_object_or_404(Compra, pk=compra_id)
    compra.delete()
    return redirect('lista_compras')

def deletar_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    venda.delete()
    return redirect('lista_vendas')