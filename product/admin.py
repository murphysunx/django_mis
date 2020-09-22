from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from .models import *


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """
    def _linkify(obj):
        app_label = obj._meta.app_label
        linked_obj = getattr(obj, field_name)
        # 检测一级类别
        try:
            model_name = linked_obj._meta.model_name
            view_name = f"admin:{app_label}_{model_name}_change"
            link_url = reverse(view_name, args=[linked_obj.cat_id])
        except Exception as e:
            link_url = ""
            linked_obj = None
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name # Sets column name
    return _linkify


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "cat_id",
        "cat_name",
        linkify(field_name="parent_id"),
    ]


admin.site.register(Product)
admin.site.register(ProductSpecs)
admin.site.register(AttrKey)
admin.site.register(AttrValue)
admin.site.register(ProductSpecsToAttrVal)
