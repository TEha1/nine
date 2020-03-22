from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Country, Category, Ad
# Register your models here.

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country', 'user', 'manage_buttons')

    def manage_buttons(self, obj):
        return format_html('<a href="{}/change/">{}</a>'' -'
                           ' ''<a href="{}/delete/">{}</a>'.
                           format(obj.id, _('update'), obj.id,_('delete')))

    manage_buttons.short_description = _('Manage')
    manage_buttons.allow_tags = True


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manage_buttons')

    def manage_buttons(self, obj):
        return format_html('<a href="{}/change/">{}</a>'' -'
                           ' ''<a href="{}/delete/">{}</a>'.
                           format(obj.id, _('update'), obj.id,_('delete')))

    manage_buttons.short_description = _('Manage')
    manage_buttons.allow_tags = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manage_buttons')

    def manage_buttons(self, obj):
        return format_html('<a href="{}/change/">{}</a>'' -'
                           ' ''<a href="{}/delete/">{}</a>'.
                           format(obj.id, _('update'), obj.id,_('delete')))

    manage_buttons.short_description = _('Manage')
    manage_buttons.allow_tags = True


