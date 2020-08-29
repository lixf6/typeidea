from django.contrib import admin

from typeidea.typeidea_source.custom_site import custom_site
from .models import Comment

# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):  # BaseOwnerAdmin
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')