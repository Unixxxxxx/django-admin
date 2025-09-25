from django.contrib import admin
from django.utils.html import format_html
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image_preview')  # 👈 show preview
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    # Method for preview
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover; border-radius:4px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'

