from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=120)
    title_slug = models.SlugField(max_length=120, unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def _flatten_submenus(self) -> str:
        return " ".join(menu.title for menu in Menu.objects.filter(parent=self))

    @property
    def submenu_items(self):
        return self.menu_set.get_queryset()

    def __str__(self) -> str:
        return f"{self.title}"


class MenuItem(Menu):
    class Meta:
        proxy = True
