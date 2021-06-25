from django.contrib import admin
from .models import Entry, Author,Blog
# Register your models here.

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
