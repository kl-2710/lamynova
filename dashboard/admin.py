from django.contrib import admin
from .models import VisitLog

@admin.register(VisitLog)
class VisitLogAdmin(admin.ModelAdmin):
    list_display = ('path', 'ip_address', 'timestamp')
    search_fields = ('path', 'ip_address')
    readonly_fields = ('path', 'ip_address', 'user_agent', 'timestamp')
    ordering = ('-timestamp',)




# Register your models here.
