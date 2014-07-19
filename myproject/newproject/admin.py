from django.contrib import admin

from newproject.models import BlogPost, BlogPostAdmin

admin.site.register(BlogPost, BlogPostAdmin)
