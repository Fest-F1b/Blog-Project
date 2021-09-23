from django.contrib import admin
from django.contrib.admin.decorators import action
from.models import(Post, Comment, Subscribe, Category_post
                   )
@admin.register(Category_post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


# for comments
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.Update(active=True)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)


# WSIWYG editor in django Admin
