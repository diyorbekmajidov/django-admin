from django.contrib import admin
from .models import (
    ConcertCategory
)

class ConcertCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ConcertCategory, ConcertCategoryAdmin)