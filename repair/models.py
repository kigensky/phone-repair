from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.


class Operating_System(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    Operating_System = models.ForeignKey(Operating_System, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_photo = CloudinaryField('image', null=True)
    bio = models.TextField()
    contact = models.CharField(max_length=60)
    user = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
            )

    def save_profile(self):
        return self.save()


    @classmethod
    def update_profile(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(profile_photo=update_details['profile_photo'],
                                               bio=update_details['bio'],
                                               contact= update_details['contact'],
                                               user=update_details['user'])

    def delete_profile(self):
        return self.delete()


    class Meta:
        ordering = ["-pk"]


    def __str__(self):
        return f'{self.user.username}'   
        
class Comment(models.Model):
    
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'