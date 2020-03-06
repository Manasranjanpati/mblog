from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','published','timestamp']
    list_editable = ['title']
    list_filter = ['updated','timestamp']
    search_fields = ['title']
    class Meta:
        model = Blog


admin.site.register(Blog, BlogAdmin)
