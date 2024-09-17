import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        
        if self.image and os.path.isfile(self.image.path):
            img = Image.open(self.image.path)
           
            img = img.resize((300, 300))
            img.save(self.image.path)  

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'


