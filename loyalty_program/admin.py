from django.contrib import admin

from loyalty_program.models import Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'credit']
    search_fields = ['user__username']

    list_filter = ['credit']
    raw_id_fields = ['user']
