from django.contrib import admin

from .models import Portfolio
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_live')

admin.site.register(Portfolio, PortfolioAdmin)
