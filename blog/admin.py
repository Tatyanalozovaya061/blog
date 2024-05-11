from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_subscription',)
    search_fields = ('pk', 'title', 'is_subscription', 'date_created',)
