from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   ROLE_CHOICES = (
      ('customer', 'Customer'),
      ('seller', 'Seller'),
      ('admin', 'Admin'),
   )

   email = models.EmailField(unique=True)
   phone_number = models.CharField(max_length=15, blank=True, null=True)

   role = models.CharField(
      max_length=20,
      choices=ROLE_CHOICES,
      default='customer'
   )
   
   is_blocked = models.BooleanField(
      default=False
   )

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']

   def __str__(self):
      return self.email
   

class Profile(models.Model):
   user = models.OneToOneField(
      User,
      on_delete=models.CASCADE,
      related_name='profile'
   )
   full_name = models.CharField(max_length=255)
   profile_image = models.ImageField(
      upload_to='profiles/',
      blank=True,
      null=True
   )
   address = models.TextField(
      blank=True,
      null=True
   )
   created_at = models.DateTimeField(
      auto_now_add=True
   )

   def __str__(self):
      return self.user.email 