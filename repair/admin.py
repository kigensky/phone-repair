from django.contrib import admin
from .models import Comment, Post,Operating_System,Profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Operating_System)
admin.site.register(Profile)
admin.site.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'title', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)