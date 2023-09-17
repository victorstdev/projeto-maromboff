from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Compra(models.Model):

    data_compra = models.DateField(_("Data da Compra"), default=timezone.now)
    produto = models.ForeignKey("app.Produto", verbose_name=_("Produto"), on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(_("Quantidade"))
    preco = models.DecimalField(_("Preço"), max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = _("Compra")
        verbose_name_plural = _("Compras")

    def __str__(self):
        return f"Compra de {self.quantidade} {self.produto} em {self.data_compra}"
    
    def get_absolute_url(self):
        return reverse("Compra_detail", kwargs={"pk": self.pk})

class Venda(models.Model):

    data_venda = models.DateField(_("Data da Venda"), default=timezone.now)
    quantidade = models.PositiveIntegerField(_("Quantidade"))
    preco_total = models.DecimalField(_("Preço total"), max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = _("Venda")
        verbose_name_plural = _("Vendas")

    def __str__(self):
        return f"Venda de {self.quantidade} banoff em {self.data_venda}"

    def get_absolute_url(self):
        return reverse("Venda_detail", kwargs={"pk": self.pk})

class Produto(models.Model):

    nome = models.CharField(_("Nome do Produto"), max_length=50)
    descricao = models.TextField(_("Descrição do Produto"))
    
    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("Produto_detail", kwargs={"pk": self.pk})
