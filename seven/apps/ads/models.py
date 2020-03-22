from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

from ..user.models import User, Country


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Ad(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_('user'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.CharField(max_length=500, verbose_name=_('description'))
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, verbose_name=_('Country'))
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    msg_allow = models.BooleanField( verbose_name=_('msg_allow'))
    pic1 = models.ImageField(verbose_name=_('pic1'))
    pic2 = models.ImageField(null=True, blank=True, verbose_name=_('pic2'))
    pic3 = models.ImageField(null=True, blank=True, verbose_name=_('pic3'))
    pic4 = models.ImageField(null=True, blank=True, verbose_name=_('pic4'))
    pic5 = models.ImageField(null=True, blank=True, verbose_name=_('pic5'))
    main = models.PositiveSmallIntegerField(default=1, verbose_name=_('main'))

    class Meta:
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")

    def __str__(self):
        return self.title
