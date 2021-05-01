from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Customize Image admin panel."""

    list_display = ["title", "image", "created"]
    list_filter = ["created"]

