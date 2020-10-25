from django.contrib import admin

from loyalty_program.models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'points']
    search_fields = ['user__username']

    list_filter = ['points']
    raw_id_fields = ['user']
