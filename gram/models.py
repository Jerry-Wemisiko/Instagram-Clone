from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")    
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    username = models.CharField( max_length=20, unique=True)  
    email = models.CharField( max_length=50, unique=True)
    name = models.CharField( max_length=50, unique=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField( max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']
 
    
    objects=MyAccountManager()
     
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


        
class Profile(models.Model):
    user = models.OneToOneField('Users', on_delete = models.CASCADE)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150,blank=True)
    bio = models.TextField()
    photo = CloudinaryField('prof',null=True,blank=True,default='img')
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user.username}'

    def save_profile(self):
        self.user.save()
        
    @classmethod
    def search_profile(cls,uname):
        return cls.object.filter(user__username__icontains=uname).all()

class Image(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    image= CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    comments = models.TextField(max_length=500, blank=True)
    likes = models.ManyToManyField(User,blank=True)

    def __str__(self) -> str:
        return f'{self.image}'

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()

    @property
    def update_caption(self):
        return self.image_caption.update()

    @property
    def comments(self):
        return self.comments.all()

    @property
    def likes(self):
        return self.likes.count()

class Comment(models.Model):
    comment = models.TextField()

    def save_comment(self):
        return self.save()

    def delete_comment(self):
        return self.delete()

    def update_comment(self):
        return self.update()



