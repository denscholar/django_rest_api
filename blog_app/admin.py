from django.contrib import admin
from .models import BlogComment, Category, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'created', 'is_public')
    list_display_links = ('id', 'blog_title')
    search_fields = ('blog_title', 'author')
    list_per_page = 2
    list_editable = ("is_public",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Category)
