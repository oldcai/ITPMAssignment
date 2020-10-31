from django.contrib import admin
from quilljs.admin import QuillAdmin

from loyalty_program.models import Credit, Offer, UserOfferApplication


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'points']
    search_fields = ['user__username']

    raw_id_fields = ['user']


@admin.register(Offer)
class OfferAdmin(QuillAdmin):
    list_display = ['title', 'price_in_points', 'enabled']

    list_filter = ['enabled']

    actions = ['enable', 'disable']

    def enable(self, request, queryset):
        queryset.update(enabled=True)

    def disable(self, request, queryset):
        queryset.update(enabled=False)


@admin.register(UserOfferApplication)
class UserOfferApplication(admin.ModelAdmin):
    list_display = ['user', 'offer', 'permitted']

    list_filter = ['permitted']

    actions = ['permit']

    def permit(self, request, queryset):
        queryset.update(permitted=True)
