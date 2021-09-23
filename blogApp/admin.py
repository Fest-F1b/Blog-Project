from django.contrib import admin
from django.contrib.admin.decorators import action
<<<<<<< HEAD
from.models import(Post, Comment, Subscribe, Category_post
                   )
@admin.register(Category_post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
=======
from.models import(Post, Comment, Subscribe
                   )
>>>>>>> fbc4e48c5a973e4301bd1924a9f9249946f9b4f5


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
<<<<<<< HEAD
    list_filter = ("status",)
=======
    list_filter = ("status","post_in_category")
>>>>>>> fbc4e48c5a973e4301bd1924a9f9249946f9b4f5
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
