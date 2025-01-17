from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 

# Custom user model extending AbstractUser
class CustomUser (AbstractUser ):
    ROLE_CHOICES = (
        ('realtor', 'Realtor'),
        ('user', 'User '),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    groups = models.ManyToManyField(Group, related_name='customuser_set') 
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions_set')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)  # Use CustomUser  here
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    birth_date = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.user.username