from django.contrib import admin

from .models import Category, Asset, Project


class AssetInline(admin.TabularInline):
    model = Asset


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        AssetInline
    ]
    fields = (
        'client_name',
        'slug',
        'description',
        'lead_art',
        'categories',
        'completion_date',
        'is_featured',
        'is_public')

    filter_horizontal = ('categories',)
    list_display = (
        'client_name',
        'completion_date',
        'is_public',
        'is_featured')
    list_display_links = ('client_name',)
    list_filter = ('is_public',)
    prepopulated_fields = {'slug': ('client_name',)}
    search_fields = ('client_name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
