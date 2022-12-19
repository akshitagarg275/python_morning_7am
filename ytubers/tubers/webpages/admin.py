from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def myPhoto(self,object):
        return format_html('<img  src = "{}" width="40">'.format(object.photo.url))

    list_display = ('myPhoto', 'first_name', 'last_name','role')
    list_display_links=('role',)
    search_fields=('role',)
    list_filter=('role','created_at')

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)