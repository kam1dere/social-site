from django.contrib import admin
from .models import Discussion


@admin.register(Discussion)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


from django.contrib import admin

# Register your models here.
