from django.contrib import admin

from .models import ShortLink


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ("path", "kind", "url", "code_date")
    list_filter = ("kind",)
    search_fields = ("path", "url")
    ordering = ("path",)

    fieldsets = (
        (
            None,
            {
                "fields": ("path", "kind"),
            },
        ),
        (
            "Redirection",
            {
                "fields": ("url",),
            },
        ),
        (
            "Génération de codes",
            {
                "fields": ("code_key", "code_date"),
            },
        ),
    )
