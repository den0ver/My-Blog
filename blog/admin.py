from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish', 'author', 'status']
    list_display_links = ['id', 'title']
    list_filter = ['author', 'status', 'publish', 'created', 'updated']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['author', 'status']
    show_facets = admin.ShowFacets.ALWAYS
