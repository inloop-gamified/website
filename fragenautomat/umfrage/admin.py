from django.contrib import admin
from django.utils.html import format_html

from umfrage.models import Violation, Medic, Rule
from umfrage.models import Umfrage, UmfrageRating


admin.site.register(Violation)
admin.site.register(Medic)
admin.site.register(Rule)

@admin.register(UmfrageRating)
class UmfrageRatingAdmin(admin.ModelAdmin):
    fields = [
        'text',
        'value',
        'is_completed',
    ]
    list_display = [
        'text',
        'value',
        'is_completed',
    ]
    list_filter = [
        'value',
        'is_completed',
        'text'
    ]
    search_fields = [
        'text',
    ]
    readonly_fields = [
        'text'
    ]

@admin.register(Umfrage)
class UmfrageAdmin(admin.ModelAdmin):
    fields = [
        'key',
        'is_completed',
    ]
    list_display = [
        'site_link',
        'get_rule',
        'is_completed',
    ]
    list_filter = [
        'is_completed',
    ]
    search_fields = [
        'key',
    ]
    readonly_fields = [
        'key'
    ]

    def get_rule(self, obj):
        return obj.violation.rule.identifier
    get_rule.short_description = 'Rule'

    def site_link(self, obj):
        return format_html(f'<a href="/umfrage/{obj.key}/" target="_blank">{obj}</a>')
    site_link.allow_tags = True
    site_link.short_description = 'View Umfrage'
