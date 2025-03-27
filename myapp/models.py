from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')
    faculty_student_id = models.CharField(max_length=20, unique=True)

    # Add related_name to avoid conflicts with Django's default User model
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username
