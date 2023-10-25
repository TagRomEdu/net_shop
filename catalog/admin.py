from django.contrib import admin

from catalog.models import Category, Product, Blog, Version
from users_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_search = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'creating_date', 'modified_date', 'user')
    list_filter = ('category',)
    list_search = ('name', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'is_published', 'view_count', 'user')
    list_search = ('name', 'text')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'num_ver', 'name_ver', 'is_version')
