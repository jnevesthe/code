from django.contrib import admin
from .models import Inf

admin.site.register(Inf)

from .models import Acesso

@admin.register(Acesso)
class AcessoMiddleware(admin.ModelAdmin):
    list_display = ['ip', 'caminho', 'data_acesso']
    list_filter = ['data_acesso', 'caminho']
    search_fields = ['ip', 'caminho']
    readonly_fields = ['ip', 'caminho', 'data_acesso']
    ordering = ['-data_acesso']
