from django.contrib import admin
from .models import Portfolio, Image, Comment

#!!!
# admin.site.register(Portfolio)
@admin.register(Portfolio)
class AdminPortfolio(admin.ModelAdmin):
    list_display = ('name', 'description', 'author', 'created', 'updated')
    list_filter = ('author', 'created')
    search_fields = ('name', 'description')


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('portfolio', 'name', 'updated', 'created')
    list_filter = ('portfolio', 'created')
    search_fields = ('name', 'description')


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('image', 'name', 'body', 'created', 'active')
    list_filter = ('image', 'created', 'active')
    search_fields = ('name', 'body')
