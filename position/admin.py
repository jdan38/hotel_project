from django.contrib import admin

from .models import Position

class PostionAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'photo', 'level', 'payrate')

admin.site.register(Position, PostionAdmin)