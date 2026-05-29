from django.contrib import admin

from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Kolumny, które będą widoczne na liście w panelu admina
    list_display = ('user', 'file_name', 'file_type', 'uploaded_at')

    # Dodanie filtrów po boku strony
    list_filter = ('file_type', 'uploaded_at')
