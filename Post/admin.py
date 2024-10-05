from django.contrib import admin

from Post.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'created', 'updated', ]
    list_filter = ['author', 'created', 'updated', ]
    readonly_fields = ['slug']
    raw_id_fields = ['author']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    readonly_fields = ['slug']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created', 'is_reply']
    raw_id_fields = ['user', 'post', 'reply']

