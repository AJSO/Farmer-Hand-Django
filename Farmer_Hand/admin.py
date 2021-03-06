from django.contrib import admin

# Register your models here.
from Farmer_Hand.models import BlogPost, Category


class BlogPostAdmin(admin.ModelAdmin):
    list_filter = ['created_at',]
    search_fields = ['title','body']
    list_display = ['title','category']

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
