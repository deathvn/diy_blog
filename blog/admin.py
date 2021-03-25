from django.contrib import admin

# Register your models here.
from .models import Blog, BlogAuthor, BlogComment

# admin.site.register(Blog)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)

class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    fields = ('description', 'author', 'post_date')
    readonly_fields = ['post_date']
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentInline]