import os
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255, blank=True)
    file_type = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        if self.photo and not self.pk:
            # Pobieramy oryginalną nazwę pliku
            self.file_name = self.photo.name

            # Wyciągamy rozszerzenie pliku
            _, extension = os.path.splitext(self.photo.name)
            self.file_type = extension.lower()

        # POPRAWIONE: Bezpośrednie wywołanie metody save klasy nadrzędnej
        super().save(*args, **kwargs)

