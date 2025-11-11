from django.contrib import admin

# Register your models here.
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'genre')
    search_fields = ('title', 'director', 'genre')
    list_filter = ('year', 'genre')
