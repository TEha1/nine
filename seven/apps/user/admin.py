from django.contrib import admin
# Models
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.utils.translation import gettext as _

from .models import User
# Register your models here.

admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'mobile', 'is_active', 'is_authenticated', 'manage_buttons')

    def manage_buttons(self, obj):
        return format_html('<a href="{}/change/">{}</a>'' -'
                           ' ''<a href="{}/delete/">{}</a>'.
                           format(obj.id, _('update'), obj.id, _('delete')))

    manage_buttons.short_description = _('Manage')
    manage_buttons.allow_tags = True
