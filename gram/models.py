from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 300)
  
  def __str__(self) -> str:
        return self.user.username
  
  @classmethod
  def search_user(cls,username):
        return User.objects.filter(username__icontains = username)

  def save_profile(self):
      self.save()

  
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
  
