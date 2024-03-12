# yourappname/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    # Add custom fields if needed
    score = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Custom Users'  # Optional: Customize the plural name

# Change the related names for groups and user_permissions to avoid clashes
CustomUser.groups.field.remote_field.related_name = "customuser_groups"
CustomUser.user_permissions.field.remote_field.related_name = "customuser_permissions"
