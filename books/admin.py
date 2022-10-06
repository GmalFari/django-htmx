from django.contrib import admin
from .models import Author,Books

# Register your models here.


class BookInlineAdmin(admin.TabularInline):
    model = Books
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]
admin.site.register(Author,AuthorAdmin)
