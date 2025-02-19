from django.contrib import admin

from ..models import PullData as Model


class ModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "queue",
        "data",
    ]
    list_filter = ["queue"]
    search_fields = [
        "queue",
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Model, ModelAdmin)
