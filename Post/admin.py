from django.contrib import admin

from Post.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'created', 'updated', ]
    # list_display_links = []
    list_filter = ['author', 'created', 'updated', ]
    # list_editable = ['title', 'slug', ]
    readonly_fields = ['slug']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    readonly_fields = ['slug']
