from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q, QuerySet

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "_flatten_submenus"]
    list_display_links = ["title"]
    search_fields = ["title"]
    fields = ["title", "title_slug"]

    def get_queryset(self, request: WSGIRequest) -> QuerySet:
        return super().get_queryset(request).filter(Q(parent=None))


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["title", "_flatten_submenus"]
    list_filter = ["parent"]
    search_fields = ["title"]

    def get_queryset(self, request: WSGIRequest) -> QuerySet:
        return super().get_queryset(request).filter(~Q(parent=None))
