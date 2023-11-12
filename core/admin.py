from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class BookAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')