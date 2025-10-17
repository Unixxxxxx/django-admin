from django.contrib import admin
from .models import Contact, new, alpha 
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "short_message", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)
    ordering = ("-created_at",) 

    def short_message(self, obj):
        return obj.message[:50] + ("..." if len(obj.message) > 50 else "")
    short_message.short_description = "Message"

@admin.register(new)
class NewAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')  
    search_fields = ('name',)  

@admin.register(alpha)
class AlphaAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)

