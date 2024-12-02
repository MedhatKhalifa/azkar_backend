from django.contrib import admin
from .models import Azkar, DatabaseVersion

@admin.register(Azkar)
class AzkarAdmin(admin.ModelAdmin):
    list_display = ['content', 'category', 'language']
    search_fields = ['content', 'category', 'language']

@admin.register(DatabaseVersion)
class DatabaseVersionAdmin(admin.ModelAdmin):
    list_display = ['version', 'updated_at']
