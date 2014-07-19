from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return self.title


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

