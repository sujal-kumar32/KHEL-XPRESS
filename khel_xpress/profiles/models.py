from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to=user_directory_path,
        default='default_images/profile.jpg',  # Ensure this file exists in MEDIA_ROOT
        null=True,
        blank=True
    )
    cover_picture = models.ImageField(
        upload_to=user_directory_path,
        default='default_images/background.jpg',  # Ensure this file exists in MEDIA_ROOT
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"