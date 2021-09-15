from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150,blank=True)
    bio = models.TextField()
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    


class Image(models.Model):
    image= CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=100,blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes =models.IntegerField()
    comments = models.TextField(max_length=500, blank=True)

    def __str__(self) -> str:
        return f'{self.image}'

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()

    def update_caption(self):
        return self.update()

# class Post(models.Model):
#     author = models.ForeignKey("auth.User" ,on_delete=models.CASCADE)
#     image = models.CloudinaryField(blank=True,null=True)


