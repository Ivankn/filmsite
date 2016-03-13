from django.contrib import admin
from .models import Category, Film, Comment, News, Actor

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','description','filmSlug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Actor, ActorAdmin)

class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'youtube', 'year', 'country', 'age', 'seasons', 'rating']
    list_filter = ['created', 'uploaded']
    list_editable = ['rating']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Film, FilmAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'film', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'body','added')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(News, NewsAdmin)
