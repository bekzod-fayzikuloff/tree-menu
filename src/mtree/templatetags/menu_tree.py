from django import template
from django.template import RequestContext

from ..models import Menu

register = template.Library()


@register.inclusion_tag(filename="templatetags/menu.html", takes_context=True)
def draw_menu(context: RequestContext, menu_slug: str):
    menu_properties = {}
    try:
        menu = (
            Menu.objects.prefetch_related(
                "menu_set",
                "menu_set__menu_set",
            )
            .select_related("parent")
            .get(title_slug=menu_slug, parent=None)
        )
        menu_properties["main"] = menu
        menu_properties["node"] = menu.menu_set.all()
    except Menu.DoesNotExist:
        menu_properties["error"] = f"Menu by {menu_slug} keyword not found"

    return {"menu": menu_properties, "request": context["request"]}


@register.inclusion_tag(filename="templatetags/submenu.html", takes_context=True)
def draw_submenu_item(context: RequestContext, submenu: Menu):
    return {"submenu": submenu, "request": context["request"]}
